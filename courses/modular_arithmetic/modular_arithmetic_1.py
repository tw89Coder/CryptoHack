# Calculate the first modulus
# 11 divided by 6, the remainder is x
x = 11 % 6

# Calculate the second modulus
# Large integer divided by 17, the remainder is y
# Python handles arbitrarily large integers automatically
y = 8146798528947 % 17

print(f"x = {x}")
print(f"y = {y}")

# The problem asks for the smaller of the two integers
flag = min(x, y)
print(f"Flag (the smaller number): {flag}")
