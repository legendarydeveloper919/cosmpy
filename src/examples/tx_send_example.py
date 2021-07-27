""" Sending and querying funds example """

from cosm.crypto.keypairs import PrivateKey
from cosm.crypto.address import Address
from cosmos.bank.v1beta1.tx_pb2 import MsgSend
from cosmos.base.v1beta1.coin_pb2 import Coin
from cosmos.bank.v1beta1.query_pb2_grpc import QueryStub as BankQueryClent
from cosmos.bank.v1beta1.query_pb2 import QueryBalanceRequest, QueryBalanceResponse

from grpc import insecure_channel
from grpc._channel import Channel

from google.protobuf.any_pb2 import Any

from examples.helpers import sign_and_broadcast_msg



def get_balance(channel: Channel, address: Address, denom: str) -> QueryBalanceResponse:
    """
    Get balance of specific account and denom

    :param channel: gRPC channel
    :param address: Address
    :param denom: Denomination

    :return: QueryBalanceResponse
    """
    bank_client = BankQueryClent(channel)
    res = bank_client.Balance(QueryBalanceRequest(address=str(address), denom=denom))
    return res


def get_packed_send_msg(from_address: Address, to_address: Address, amount: [Coin]):
    """
    Generate and pack MsgSend

    :param from_address: Address of sender
    :param to_address: Address of recipient
    :param amount: List of Coins to be sent

    :return: packer Any type message
    """
    msg_send = MsgSend(from_address=str(from_address),
                       to_address=str(to_address),
                       amount=amount)
    send_msg_packed = Any()
    send_msg_packed.Pack(msg_send, type_url_prefix="/")

    return send_msg_packed


# Denomination and amouunt of transferred tokens
DENOM = "stake"
AMOUNT = [Coin(amount="1", denom=DENOM)]

# Private key of sender's account
FROM_PK = PrivateKey(
    bytes.fromhex(
        "0ba1db680226f19d4a2ea64a1c0ea40d1ffa3cb98532a9fa366994bb689a34ae"
    )
)
FROM_ADDRESS = Address(FROM_PK)

# Address of recipient account
TO_ADDRESS = "fetch128r83uvcxns82535d3da5wmfvhc2e5mut922dw"

# Open gRPC channel
channel = insecure_channel("localhost:9090")

# Print balance before transfer
print("Before transaction")
res = get_balance(channel, FROM_ADDRESS, DENOM)
print(f"Validator has {res.balance.amount} {DENOM}")
res = get_balance(channel, FROM_ADDRESS, DENOM)
print(f"Bob has {res.balance.amount} {DENOM}")

# Create send message
msg = get_packed_send_msg(from_address=FROM_ADDRESS,
                          to_address=TO_ADDRESS,
                          amount=AMOUNT)

# Send and broadcast message
sign_and_broadcast_msg(msg, channel, FROM_PK)

# Print balance after transfer
print("After transaction")
res = get_balance(channel, FROM_ADDRESS, DENOM)
print(f"Validator has {res.balance.amount} {DENOM}")
res = get_balance(channel, TO_ADDRESS, DENOM)
print(f"Bob has {res.balance.amount} {DENOM}")
