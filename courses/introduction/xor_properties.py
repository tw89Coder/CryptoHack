# CryptoHack Course: Introduction -> XOR Properties
from pwn import xor

# Hex strings provided by the challenge
v1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
v2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e" # KEY2 ^ KEY1
v3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1" # KEY2 ^ KEY3
v4 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf" # FLAG ^ KEY1 ^ KEY3 ^ KEY2

# Convert hex to bytes
v1_b = bytes.fromhex(v1)
v2_b = bytes.fromhex(v2)
v3_b = bytes.fromhex(v3)
v4_b = bytes.fromhex(v4)

# Apply XOR properties to isolate the FLAG
# FLAG = v4 ^ v2 ^ v3
# Reason: v4 ^ v2 ^ v3 = (F ^ K1 ^ K3 ^ K2) ^ (K2 ^ K1) ^ (K2 ^ K3) = F ^ K2
# Then: (F ^ K2) ^ KEY2
# Let's use a simpler path:
key2 = xor(v2_b, v1_b)
key3 = xor(v3_b, key2)
flag = xor(v4_b, v1_b, key2, key3)

print(f"Flag: {flag.decode()}")