"""
CryptoHack Challenge: Modular Inverting
Goal: Find the inverse element 'd' such that 3 * d = 1 mod 13.
"""

def solve_modular_inverse():
    # Given values
    g = 3   # The element to invert
    p = 13  # The modulus (prime number)

    print(f"Goal: Find d such that {g} * d == 1 (mod {p})")
    print("-" * 40)

    # ---------------------------------------------------------
    # Method 1: Theoretical Approach (Fermat's Little Theorem)
    # ---------------------------------------------------------
    # Theory: 
    # If p is prime, then g^(p-1) == 1 (mod p).
    # We can rewrite this as: g * g^(p-2) == 1 (mod p).
    # Therefore, the inverse of g is g^(p-2).
    
    d_fermat = pow(g, p - 2, p)
    
    print("Method 1: Fermat's Little Theorem")
    print(f"Formula: g^(p-2) mod p")
    print(f"Calculation: {g}^({p}-2) mod {p} = {d_fermat}")
    print("-" * 40)

    # ---------------------------------------------------------
    # Method 2: Fastest Implementation (Python Built-in)
    # ---------------------------------------------------------
    # Python's pow(base, exp, mod) function supports modular inverse natively.
    # By passing -1 as the exponent, Python calculates the modular inverse.
    # Note: This is generally implemented using the Extended Euclidean Algorithm,
    # so it works efficiently even for very large numbers.
    
    d_python = pow(g, -1, p)
    
    print("Method 2: Python Built-in (Recommended for CTF)")
    print(f"Code: pow({g}, -1, {p})")
    print(f"Result: {d_python}")
    print("-" * 40)

    # ---------------------------------------------------------
    # Verification
    # ---------------------------------------------------------
    check = (g * d_python) % p
    print(f"Verification: {g} * {d_python} = {g * d_python}")
    print(f"Mod Result: {g * d_python} % {p} = {check}")
    
    if check == 1:
        print(">> SUCCESS: The inverse is correct.")
    else:
        print(">> FAILURE: Something went wrong.")

if __name__ == "__main__":
    solve_modular_inverse()
