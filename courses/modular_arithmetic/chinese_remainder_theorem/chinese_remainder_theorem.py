from functools import reduce

def extended_gcd(a, b):
    """
    Standard Extended Euclidean Algorithm to find modular inverse.
    Returns (g, x, y) such that a*x + b*y = g
    """
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_gcd(b % a, a)
        return g, x - (b // a) * y, y

def inverse(a, m):
    """
    Finds the modular inverse of a modulo m using Extended GCD.
    Returns x such that (a * x) % m == 1
    """
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    return x % m

def solve_crt(congruences):
    """
    Solves the Chinese Remainder Theorem for a list of congruences.
    
    Arguments:
        congruences: A list of tuples (remainder, modulus)
                     e.g., [(2, 5), (3, 11), (5, 17)]
                     meaning x = 2 mod 5, x = 3 mod 11, etc.
    """
    
    # 1. Calculate the product of all moduli (N)
    # Using reduce to multiply all moduli together
    # N = 5 * 11 * 17 = 935
    N = reduce(lambda x, y: x * y, [m for r, m in congruences])
    
    print(f"Total Modulus N = {N}")
    
    final_result = 0
    
    # 2. Iterate through each equation to apply Gauss's algorithm
    # Formula: x = sum(a_i * N_i * y_i) mod N
    print("-" * 40)
    print(f"{'Remainder (a)':<15} {'Modulus (n)':<15} {'Ni (N/n)':<15} {'Inverse (y)':<15}")
    print("-" * 40)

    for a_i, n_i in congruences:
        # Calculate N_i: The product of all other moduli
        N_i = N // n_i
        
        # Calculate y_i: The modular inverse of N_i modulo n_i
        # We need N_i * y_i = 1 (mod n_i)
        y_i = inverse(N_i, n_i)
        
        # Add the contribution of this part to the sum
        term = a_i * N_i * y_i
        final_result += term
        
        print(f"{a_i:<15} {n_i:<15} {N_i:<15} {y_i:<15}")

    print("-" * 40)
    
    # 3. Final step: Take the sum modulo N
    return final_result % N

# --- Main Execution ---

# Problem:
# x = 2 mod 5
# x = 3 mod 11
# x = 5 mod 17
challenges = [
    (2, 5),
    (3, 11),
    (5, 17)
]

print("Solving Chinese Remainder Theorem...")
x = solve_crt(challenges)

print(f"\nCalculated x: {x}")

# Verification
print("\nVerification:")
for r, m in challenges:
    check = x % m
    print(f"{x} % {m} = {check} (Expected: {r}) -> {'OK' if check == r else 'FAIL'}")

print(f"\nFlag: {x}")
