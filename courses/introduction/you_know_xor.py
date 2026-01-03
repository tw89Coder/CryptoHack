# CryptoHack Course: Introduction -> You either know, XOR you don't
from pwn import xor

hex_input = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
ciphertext = bytes.fromhex(hex_input)

# Step 1: Recover the partial key using the known flag format "crypto{"
known_prefix = b"crypto{"
partial_key = xor(ciphertext[:len(known_prefix)], known_prefix)

print(f"Partial key found: {partial_key.decode()}")

# Step 2: From the output, we can guess the full repeating key.
# If partial_key is 'myXORke', the full key is likely 'myXORkey'
# Let's try adding the missing 'y' and the closing '}' to verify.
full_key = b"myXORkey" # This is a common pattern in this challenge

# Step 3: Decrypt the entire ciphertext with the full repeating key
flag = xor(ciphertext, full_key)
print(f"Flag: {flag.decode()}")
