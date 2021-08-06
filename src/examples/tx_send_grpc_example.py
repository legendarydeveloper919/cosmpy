""" gRPC example of sending and querying funds """

from cosm.crypto.keypairs import PrivateKey
from cosmos.base.v1beta1.coin_pb2 import Coin

from cosm.clients.signing_cosmwasm_client import SigningCosmWasmClient
from grpc import insecure_channel

# Denomination and amount of transferred tokens
DENOM = "stake"
AMOUNT = [Coin(amount="1", denom=DENOM)]

# Node config
GRPC_ENDPOINT_ADDRESS = "localhost:9090"
CHAIN_ID = "testing"

# Private key of sender's account
FROM_PK = PrivateKey(
    bytes.fromhex(
        "0ba1db680226f19d4a2ea64a1c0ea40d1ffa3cb98532a9fa366994bb689a34ae"
    )
)
# Create client
channel = insecure_channel(GRPC_ENDPOINT_ADDRESS)
client = SigningCosmWasmClient(FROM_PK, channel, CHAIN_ID)

# Address of recipient account
TO_ADDRESS = "fetch128r83uvcxns82535d3da5wmfvhc2e5mut922dw"

# Print balance before transfer
print("Before transaction")
res = client.get_balance(client.address, DENOM)
print(f"Validator has {res.balance.amount} {DENOM}")
res = client.get_balance(TO_ADDRESS, DENOM)
print(f"Bob has {res.balance.amount} {DENOM}")

# Generate, sign and broadcast send tokens transaction
client.send_tokens(TO_ADDRESS, AMOUNT)

# Print balance after transfer
print("After transaction")
res = client.get_balance(client.address, DENOM)
print(f"Validator has {res.balance.amount} {DENOM}")
res = client.get_balance(TO_ADDRESS, DENOM)
print(f"Bob has {res.balance.amount} {DENOM}")
