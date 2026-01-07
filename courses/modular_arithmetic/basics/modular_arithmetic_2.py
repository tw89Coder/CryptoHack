# Part 1: Verify small examples given in the problem
p = 17
print(f"3^17 mod 17 = {pow(3, 17, 17)}")  # Expected: 3
print(f"5^17 mod 17 = {pow(5, 17, 17)}")  # Expected: 5
print(f"7^16 mod 17 = {pow(7, 16, 17)}")  # Expected: 1 (Because 16 is p-1)

# Part 2: The actual flag challenge
# p = 65537 is a prime number
large_base = 273246787654
large_mod = 65537
exponent = 65536  # This is large_mod - 1

# According to Fermat's Little Theorem, the result should be 1
result = pow(large_base, exponent, large_mod)

print(f"Flag (Result of the large calculation): {result}")
