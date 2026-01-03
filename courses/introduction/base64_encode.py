# CryptoHack Course: Introduction -> Base64
import base64

hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Step 1: Convert Hex back to Bytes
raw_bytes = bytes.fromhex(hex_string)

# Step 2: Encode Bytes into Base64
# b64encode also returns bytes, so we need to use .decode() to convert it to a string for easier viewing of the result
b64_output = base64.b64encode(raw_bytes).decode()

print(f"Base64 Result: {b64_output}")