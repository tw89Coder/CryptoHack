# CryptoHack Course: Introduction -> XOR Starter

data = "label"
key = 13

# Method 1: Manual implementation using a list comprehension
# 1. ord(char) converts character to its Unicode/ASCII integer
# 2. ^ key performs the bitwise XOR with 13
# 3. chr(...) converts the resulting integer back to a character
output_chars = [chr(ord(c) ^ key) for c in data]
new_string = "".join(output_chars)

# The flag format is crypto{new_string}
print(f"crypto{{{new_string}}}")