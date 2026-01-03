# CryptoHack Course: Introduction -> Favourite byte
from pwn import xor

hex_input = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
data = bytes.fromhex(hex_input)

# Brute force all possible single-byte keys (0-255)
for key in range(256):
    # pwntools xor() can handle (bytes, int)
    decrypted = xor(data, key)
    
    # Check if the decrypted result starts with the known flag format
    if b"crypto{" in decrypted:
        print(f"Key found: {key}")
        print(f"Flag: {decrypted.decode()}")
        break