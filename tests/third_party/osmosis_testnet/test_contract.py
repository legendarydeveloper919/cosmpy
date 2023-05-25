# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2022 Fetch.AI Limited
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

"""Osmosis contract test."""
from cosmpy.aerial.client import LedgerClient
from cosmpy.aerial.wallet import LocalWallet

from tests.integration.test_contract import TestContract as BaseTestContract
from tests.third_party.osmosis_testnet.net_config import (
    COIN,
    FaucetMixIn,
    GAS_LIMIT,
    NET_CONFIG,
    PREFIX,
)


class TestContract(BaseTestContract, FaucetMixIn):
    """Test contract

    :param BaseTestContract: Base test contract
    :param FaucetMixIn: Osmosis Faucet config
    """

    COIN = COIN
    GAS_LIMIT = GAS_LIMIT
    PREFIX = PREFIX

    def get_ledger(self):
        return LedgerClient(NET_CONFIG)

    def get_wallet(self):
        wallet = LocalWallet.generate(prefix=PREFIX)
        self.ask_funds(wallet, self.get_ledger(), 100000000)
        return wallet
