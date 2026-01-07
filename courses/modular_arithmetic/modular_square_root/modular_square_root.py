import re

FILENAME = "output_modular_square_root.txt"

def parse_file(filename):
    """
    Robust parser to extract 'a' and 'p' from the formatted text file.
    Handles multi-line integers and formatting characters.
    """
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        # Remove all whitespace and newlines to merge multi-line numbers
        clean_content = "".join(content.split())
        
        # Regex to find a=... and p=...
        a_match = re.search(r'a=(\d+)', clean_content)
        p_match = re.search(r'p=(\d+)', clean_content)
        
        if not a_match or not p_match:
            raise ValueError("Could not find 'a' or 'p' in the file.")
            
        a = int(a_match.group(1))
        p = int(p_match.group(1))
        
        return a, p

    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        exit(1)

def legendre_symbol(a, p):
    """
    Computes the Legendre symbol (a/p).
    Returns 1 if a is a quadratic residue, -1 if not, 0 if a is 0 mod p.
    """
    return pow(a, (p - 1) // 2, p)

def tonelli_shanks(n, p):
    """
    Finds x such that x^2 = n (mod p) using the Tonelli-Shanks algorithm.
    """
    # 1. Check if n is a quadratic residue
    ls = legendre_symbol(n, p)
    if ls != 1:
        if n == 0: return 0
        return None # No square root exists

    # 2. Simple case: p = 3 mod 4
    if p % 4 == 3:
        return pow(n, (p + 1) // 4, p)

    # 3. Tonelli-Shanks Algorithm (for p = 1 mod 4)
    
    # Step 1: Write p-1 = Q * 2^S, with Q odd
    s = 0
    q = p - 1
    while q % 2 == 0:
        q //= 2
        s += 1
        
    # Step 2: Find a quadratic non-residue z
    z = 2
    while legendre_symbol(z, p) != p - 1: # p-1 is congruent to -1
        z += 1
        
    # Step 3: Initialize variables
    m = s
    c = pow(z, q, p)
    t = pow(n, q, p)
    r = pow(n, (q + 1) // 2, p)
    
    # Step 4: Loop
    while True:
        if t == 0: return 0
        if t == 1: return r
        
        # Find the lowest i (0 < i < m) such that t^(2^i) = 1
        t2i = t
        i = 0
        for i in range(1, m):
            t2i = (t2i * t2i) % p
            if t2i == 1:
                break
        
        # If no such i is found, something is wrong (shouldn't happen for valid inputs)
        if i == m: return None 
        
        # Calculate b = c^(2^(m-i-1))
        b = c
        for _ in range(m - i - 1):
            b = (b * b) % p
            
        m = i
        c = (b * b) % p
        t = (t * c) % p
        r = (r * b) % p

def solve():
    print(f"Reading from {FILENAME}...")
    a, p = parse_file(FILENAME)
    
    print(f"a = {str(a)[:30]}...")
    print(f"p = {str(p)[:30]}...")
    print("-" * 40)
    
    # Check modulo type
    if p % 4 == 1:
        print("p is congruent to 1 mod 4. Using Tonelli-Shanks algorithm.")
    else:
        print("p is congruent to 3 mod 4. Simple formula would suffice.")

    print("Calculating square root...")
    
    # Find one root
    root1 = tonelli_shanks(a, p)
    
    if root1 is None:
        print("No square root found!")
        return

    # The other root is p - root1
    root2 = p - root1
    
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
    
    # Verify
    if (root1 * root1) % p == a:
        print("Verification Successful!")
    else:
        print("Verification Failed!")
        
    print("-" * 40)
    flag = min(root1, root2)
    print("FLAG (smaller root):")
    print(flag)

if __name__ == "__main__":
    solve()
