# CryptoHack Course: Introduction -> Bytes and Big Integers
from Crypto.Util.number import *

# The large integer provided by the challenge
target_int = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

# Convert the long integer back to bytes
# long_to_bytes() handles the conversion from base-10 to base-256 (bytes)
flag_bytes = long_to_bytes(target_int)

# Decode bytes to a human-readable string
flag = flag_bytes.decode()

print(f"Flag: {flag}")