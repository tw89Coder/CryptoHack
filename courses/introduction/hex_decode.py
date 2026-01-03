# CryptoHack Course: Introduction -> Hex
hex_string = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

# bytes.fromhex() automatically processes Hexes grouped into pairs of bytes.
# .decode() converts bytes back into a string that we can understand.
flag = bytes.fromhex(hex_string).decode()

print(f"Flag: {flag}")
