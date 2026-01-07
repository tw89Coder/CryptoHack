def extended_gcd(a, b):
    """
    Calculates the Extended GCD using an iterative approach.
    This avoids Python's recursion depth limit.
    
    Returns (g, x, y) such that a*x + b*y = g
    """
    
    # Initialize coefficients
    # old_s, s correspond to the coefficient of 'a'
    # old_t, t correspond to the coefficient of 'b'
    old_s, s = 1, 0
    old_t, t = 0, 1
    old_r, r = a, b

    while r != 0:
        quotient = old_r // r
        
        # Update remainders (standard Euclidean algorithm)
        old_r, r = r, old_r - quotient * r
        
        # Update coefficients 's' (for a)
        old_s, s = s, old_s - quotient * s
        
        # Update coefficients 't' (for b)
        old_t, t = t, old_t - quotient * t

    # old_r is the GCD
    # old_s is the coefficient for a
    # old_t is the coefficient for b
    return old_r, old_s, old_t

# --- Main Execution ---

# Given values from the problem
p = 26513
q = 32321

# Find u, v such that p*u + q*v = gcd(p, q)
gcd_val, u, v = extended_gcd(p, q)

print(f"p = {p}, q = {q}")
print(f"Calculated GCD: {gcd_val}")
print(f"Coefficient u: {u}")
print(f"Coefficient v: {v}")

# Verification
equation_result = p * u + q * v
print(f"Verification (p*u + q*v): {equation_result}")

# The flag is the lower number of u and v
flag = min(u, v)
print(f"Flag (the lower number): {flag}")
