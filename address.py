from web3 import Web3
from eth_utils import keccak, to_checksum_address
from rlp import encode
from rlp.sedes import big_endian_int, Binary

# Define the sender's address and nonce
sender_address = '0x1234567890abcdef1234567890abcdef12345678'
nonce = 1

# Convert the sender's address to bytes
sender_address_bytes = bytes.fromhex(sender_address[2:])

# RLP encode the sender's address and nonce
encoded = encode([sender_address_bytes, nonce])

# Compute the keccak256 hash
contract_address_hash = keccak(encoded)

# The contract address is the last 20 bytes of the hash
contract_address = to_checksum_address(contract_address_hash[-20:])

print(f"Predicted contract address: {contract_address}")
