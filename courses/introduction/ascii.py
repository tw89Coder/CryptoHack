# CryptoHack Course: Introduction -> ASCII
# Integer array provided by the problem
data = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

# Use chr() to convert to characters and combine them
# ord() converts characters to numbers, chr() converts numbers to characters
flag = "".join(chr(c) for c in data)

print(f"Flag: {flag}")