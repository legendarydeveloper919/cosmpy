# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2021 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

import re
import time
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Optional, Tuple

import certifi
import grpc

from cosmpy.aerial.client.bank import create_bank_send_msg
from cosmpy.aerial.config import NetworkConfig
from cosmpy.aerial.exceptions import (
    BroadcastError,
    InsufficientFeesError,
    NotFoundError,
    OutOfGasError,
    QueryTimeoutError,
)
from cosmpy.aerial.gas import GasStrategy, OfflineMessageTableStrategy
from cosmpy.aerial.tx import SigningCfg, Transaction
from cosmpy.aerial.tx_helpers import MessageLog, SubmittedTx, TxResponse
from cosmpy.aerial.urls import Protocol, parse_url
from cosmpy.aerial.wallet import Wallet
from cosmpy.auth.rest_client import AuthRestClient
from cosmpy.bank.rest_client import BankRestClient
from cosmpy.common.rest_client import RestClient
from cosmpy.cosmwasm.rest_client import CosmWasmRestClient
from cosmpy.crypto.address import Address
from cosmpy.protos.cosmos.auth.v1beta1.auth_pb2 import BaseAccount
from cosmpy.protos.cosmos.auth.v1beta1.query_pb2 import QueryAccountRequest
from cosmpy.protos.cosmos.auth.v1beta1.query_pb2_grpc import QueryStub as AuthGrpcClient
from cosmpy.protos.cosmos.bank.v1beta1.query_pb2 import QueryBalanceRequest
from cosmpy.protos.cosmos.bank.v1beta1.query_pb2_grpc import QueryStub as BankGrpcClient
from cosmpy.protos.cosmos.staking.v1beta1.query_pb2_grpc import (
    QueryStub as StakingGrpcClient,
)
from cosmpy.protos.cosmos.tx.v1beta1.service_pb2 import (
    BroadcastMode,
    BroadcastTxRequest,
    GetTxRequest,
)
from cosmpy.protos.cosmos.tx.v1beta1.service_pb2_grpc import ServiceStub as TxGrpcClient
from cosmpy.protos.cosmwasm.wasm.v1.query_pb2_grpc import (
    QueryStub as CosmWasmGrpcClient,
)
from cosmpy.staking.rest_client import StakingRestClient
from cosmpy.tx.rest_client import TxRestClient

DEFAULT_QUERY_TIMEOUT_SECS = 15
DEFAULT_QUERY_INTERVAL_SECS = 2


@dataclass
class Account:
    address: Address
    number: int
    sequence: int


class LedgerClient:
    def __init__(self, cfg: NetworkConfig):
        cfg.validate()
        self._network_config = cfg

        self._gas_strategy: GasStrategy = OfflineMessageTableStrategy.default_table()

        parsed_url = parse_url(cfg.url)

        if parsed_url.protocol == Protocol.GRPC:
            if parsed_url.secure:
                with open(certifi.where(), "rb") as f:
                    trusted_certs = f.read()
                credentials = grpc.ssl_channel_credentials(
                    root_certificates=trusted_certs
                )
                grpc_client = grpc.secure_channel(parsed_url.host_and_port, credentials)
            else:
                grpc_client = grpc.insecure_channel(parsed_url.host_and_port)

            self.wasm = CosmWasmGrpcClient(grpc_client)
            self.auth = AuthGrpcClient(grpc_client)
            self.txs = TxGrpcClient(grpc_client)
            self.bank = BankGrpcClient(grpc_client)
            self.staking = StakingGrpcClient(grpc_client)
        else:
            rest_client = RestClient(parsed_url.rest_url)

            self.wasm = CosmWasmRestClient(rest_client)  # type: ignore
            self.auth = AuthRestClient(rest_client)  # type: ignore
            self.txs = TxRestClient(rest_client)  # type: ignore
            self.bank = BankRestClient(rest_client)  # type: ignore
            self.staking = StakingRestClient(rest_client)  # type: ignore

    @property
    def network_config(self) -> NetworkConfig:
        return self._network_config

    @property
    def gas_strategy(self) -> GasStrategy:
        return self._gas_strategy

    @gas_strategy.setter
    def gas_strategy(self, strategy: GasStrategy):
        if not isinstance(strategy, GasStrategy):
            raise RuntimeError("Invalid strategy must implement GasStrategy interface")
        self._gas_strategy = strategy

    def query_account(self, address: Address) -> Account:
        request = QueryAccountRequest(address=str(address))
        response = self.auth.Account(request)

        account = BaseAccount()
        if not response.account.Is(BaseAccount.DESCRIPTOR):
            raise RuntimeError("Unexpected account type returned from query")
        response.account.Unpack(account)

        return Account(
            address=address,
            number=account.account_number,
            sequence=account.sequence,
        )

    def query_bank_balance(self, address: Address, denom: Optional[str] = None) -> int:
        denom = denom or self.network_config.fee_denomination

        req = QueryBalanceRequest(
            address=str(address),
            denom=denom,
        )

        resp = self.bank.Balance(req)
        assert resp.balance.denom == denom  # sanity check

        return int(resp.balance.amount)

    def send_tokens(
        self,
        destination: Address,
        amount: int,
        denom: str,
        sender: Wallet,
        memo: Optional[str] = None,
        gas_limit: Optional[int] = None,
    ) -> SubmittedTx:

        # query the account information for the sender
        account = self.query_account(sender.address())

        # build up the store transaction
        tx = Transaction()
        tx.add_message(
            create_bank_send_msg(sender.address(), destination, amount, denom)
        )

        # estimate the fee required for this transaction
        gas_limit, fee = self.estimate_gas_and_fee_for_tx(tx)

        tx.seal(
            SigningCfg.direct(sender.public_key(), account.sequence),
            fee=fee,
            gas_limit=gas_limit,
            memo=memo,
        )
        tx.sign(sender.signer(), self.network_config.chain_id, account.number)
        tx.complete()

        # broadcast the store transaction
        return self.broadcast_tx(tx)

    def estimate_gas_for_tx(self, tx: Transaction) -> int:
        return self._gas_strategy.estimate_gas(tx)

    def estimate_fee_from_gas(self, gas_limit: int) -> str:
        return f"{gas_limit * self.network_config.fee_minimum_gas_price}{self.network_config.fee_denomination}"

    def estimate_gas_and_fee_for_tx(self, tx: Transaction) -> Tuple[int, str]:
        gas_estimate = self.estimate_gas_for_tx(tx)
        fee = self.estimate_fee_from_gas(gas_estimate)
        return gas_estimate, fee

    def wait_for_query_tx(
        self,
        tx_hash: str,
        timeout: Optional[timedelta] = None,
        internal: Optional[timedelta] = None,
    ) -> TxResponse:
        timeout = timeout or timedelta(seconds=DEFAULT_QUERY_TIMEOUT_SECS)
        internal = internal or timedelta(seconds=DEFAULT_QUERY_INTERVAL_SECS)

        start = datetime.now()
        while True:
            try:
                return self.query_tx(tx_hash)
            except NotFoundError:
                pass

            delta = datetime.now() - start
            if delta >= timeout:
                raise QueryTimeoutError()

            time.sleep(internal.total_seconds())

    def query_tx(self, tx_hash: str) -> TxResponse:
        req = GetTxRequest(hash=tx_hash)

        try:
            resp = self.txs.GetTx(req)
        except grpc.RpcError as e:
            details = e.details()
            if "not found" in details:
                raise NotFoundError()
            else:
                raise

        # parse the transaction logs
        logs = []
        for log_data in resp.tx_response.logs:
            events = {}
            for event in log_data.events:
                events[event.type] = {a.key: a.value for a in event.attributes}
            logs.append(
                MessageLog(
                    index=int(log_data.msg_index), log=log_data.msg_index, events=events
                )
            )

        # parse the transaction events
        events = {}
        for event in resp.tx_response.events:
            event_data = events.get(event.type, {})
            for attribute in event.attributes:
                event_data[attribute.key.decode()] = attribute.value.decode()
            events[event.type] = event_data

        return TxResponse(
            hash=tx_hash,
            height=int(resp.tx_response.height),
            code=int(resp.tx_response.code),
            gas_wanted=int(resp.tx_response.gas_wanted),
            gas_used=int(resp.tx_response.gas_used),
            raw_log=str(resp.tx_response.raw_log),
            logs=logs,
            events=events,
        )

    def broadcast_tx(self, tx: Transaction) -> SubmittedTx:
        # create the broadcast request
        broadcast_req = BroadcastTxRequest(
            tx_bytes=tx.tx.SerializeToString(), mode=BroadcastMode.BROADCAST_MODE_SYNC
        )

        # broadcast the transaction
        resp = self.txs.BroadcastTx(broadcast_req)
        tx_digest = resp.tx_response.txhash

        # process the response
        if resp.tx_response.code:
            if "out of gas" in resp.tx_response.raw_log:
                match = re.search(
                    r"gasWanted:\s*(\d+).*?gasUsed:\s*(\d+)", resp.tx_response.raw_log
                )
                if match is not None:
                    gas_wanted = int(match.group(1))
                    gas_used = int(match.group(2))
                else:
                    gas_wanted = -1
                    gas_used = -1

                raise OutOfGasError(tx_digest, gas_wanted=gas_wanted, gas_used=gas_used)
            elif "insufficient fees" in resp.tx_response.raw_log:
                match = re.search(r"required:\s*(\d+\w+)", resp.tx_response.raw_log)
                if match is not None:
                    required_fee = match.group(1)
                else:
                    required_fee = f"more than {tx.fee}"
                raise InsufficientFeesError(tx_digest, required_fee)
            else:
                raise BroadcastError(tx_digest, resp.tx_response.raw_log)

        return SubmittedTx(self, tx_digest)
