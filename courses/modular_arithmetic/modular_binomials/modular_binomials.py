import re
import math

FILENAME = "data_modular_binomials.txt"

def parse_file(filename):
    """
    Reads N, e1, e2, c1, c2 from the file.
    """
    data = {}
    with open(filename, 'r') as f:
        content = "".join(f.read().split()) # Remove all whitespace
        
        # Regex to extract variable assignments
        # Finds patterns like 'var=123...'
        matches = re.findall(r'([a-zA-Z0-9_]+)=(\d+)', content)
        
        for key, val in matches:
            data[key] = int(val)
            
    return data

def solve():
    print(f"Reading data from {FILENAME}...")
    data = parse_file(FILENAME)
    
    N = data['N']
    e1 = data['e1']
    e2 = data['e2']
    c1 = data['c1']
    c2 = data['c2']
    
    print("Data loaded successfully.")
    print("-" * 40)
    
    # Mathematical Logic:
    # We derived that p must divide the value K:
    # K = c1^e2 * 7^(e1*e2) - c2^e1 * 3^(e1*e2)  (mod N)
    #
    # Derivation Recap:
    # 1. c1 = (2p + 3q)^e1 = (3q)^e1 (mod p)
    # 2. c2 = (5p + 7q)^e2 = (7q)^e2 (mod p)
    # 3. Raise c1 to power e2: c1^e2 = 3^(e1*e2) * q^(e1*e2) (mod p)
    # 4. Raise c2 to power e1: c2^e1 = 7^(e1*e2) * q^(e1*e2) (mod p)
    # 5. Isolate q term and equate them.
    #    c1^e2 * 3^(-e1*e2) = q^(...) = c2^e1 * 7^(-e1*e2) (mod p)
    # 6. Cross multiply to avoid modular inverse issues:
    #    c1^e2 * 7^(e1*e2) = c2^e1 * 3^(e1*e2) (mod p)
    # 7. Therefore, the difference is a multiple of p.
    
    print("Calculating term 1: (c1 * 7^e1)^e2 mod N...")
    # Optimization: 
    # Instead of computing huge powers directly, we compute:
    # K = (c1^e2 * (7^e1)^e2) - (c2^e1 * (3^e2)^e1) 
    # Actually simpler:
    # term1 = (c1 * 7^e1)^e2
    # But wait, base logic:
    # c1^e2 * 7^(e1*e2) = (c1 * 7^e1)^e2
    # This is slightly risky if moduli don't match, but we calculate mod N
    # to keep numbers "small" (relative to infinity, still 2048 bits).
    
    # Let's calculate parts carefully modulo N
    
    # Part A: c1^e2 * 7^(e1*e2)
    # = (c1 * pow(7, e1, N))^e2 % N
    term1 = pow(c1 * pow(7, e1, N), e2, N)
    
    # Part B: c2^e1 * 3^(e1*e2)
    # = (c2 * pow(3, e2, N))^e1 % N
    term2 = pow(c2 * pow(3, e2, N), e1, N)
    
    print("Calculating Difference K...")
    K = (term1 - term2) % N
    
    print("Calculating GCD(K, N)...")
    # p is a factor of both K and N
    p = math.gcd(K, N)
    
    if p == 1 or p == N:
        print("Failed to factorize. The GCD strategy didn't yield a proper factor.")
        # Try the other modulus case (mod q) just in case logic was swapped
        # q divides: c1^e2 * 5^(e1e2) - c2^e1 * 2^(e1e2)
        print("Trying alternative (mod q logic)...")
        term3 = pow(c1 * pow(5, e1, N), e2, N)
        term4 = pow(c2 * pow(2, e2, N), e1, N)
        K2 = (term3 - term4) % N
        p_or_q = math.gcd(K2, N)
        
        if p_or_q != 1 and p_or_q != N:
             p = p_or_q
             print(f"Success with alternative logic!")
        else:
             print("Both attempts failed.")
             return
    else:
        print("Success! Factor p found.")

    q = N // p
    
    print("-" * 40)
    print("Success! Factors found.")
    print(f"p = {p}")
    print(f"q = {q}")
    print("-" * 40)
    
    flag = f"crypto{{{p},{q}}}"
    print("Here is your flag:")
    print(flag)

if __name__ == "__main__":
    solve()
