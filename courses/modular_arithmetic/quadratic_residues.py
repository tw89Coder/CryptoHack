"""
CryptoHack Challenge: Quadratic Residues
Goal: Find which integer in the list is a quadratic residue mod 29, 
and find its smaller square root.
"""

p = 29
ints = [14, 6, 11]

print(f"Checking integers {ints} modulo {p}...")
print("-" * 40)

# Brute force strategy:
# Since p is small (29), we can simply iterate through all possible roots 'a'.
# Range is 1 to 28 (p-1).
for a in range(1, p):
    # Calculate a^2 mod p
    residue = (a * a) % p
    
    # Check if this calculated residue is in our target list
    if residue in ints:
        print(f">> Match Found!")
        print(f"The Quadratic Residue is: {residue}")
        print(f"One square root is a = {a}")
        
        # Quadratic equations have two roots: a and -a (which is p - a)
        # Example: if 8^2 = 6, then (-8)^2 = 6 too. -8 mod 29 is 21.
        root2 = p - a
        print(f"The other root is -a = {root2}")
        
        # The flag is the smaller of the two roots
        flag = min(a, root2)
        print(f"Flag (smaller root): {flag}")
        break
