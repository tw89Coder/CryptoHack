import re
import math

# File path verification
FILENAME = "output_legendre_symbol.txt"

def parse_challenge_file(filename):
    """
    Reads the file and extracts 'p' and the list 'ints'.
    This parser is designed to be robust against formatting noise 
    (like line numbers, box drawing characters, or newlines).
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. Clean up the content
        # Remove all newlines and whitespace to handle multi-line lists easily
        clean_content = "".join(content.split())
        
        # 2. Extract 'p' using Regular Expression
        # Look for "p=" followed by digits
        p_match = re.search(r'p=(\d+)', clean_content)
        if not p_match:
            raise ValueError("Could not find variable 'p' in the file.")
        p = int(p_match.group(1))

        # 3. Extract 'ints'
        # Look for "ints=[" followed by content until "]"
        ints_match = re.search(r'ints=\[(.*?)\]', clean_content)
        if not ints_match:
            raise ValueError("Could not find list 'ints' in the file.")
            
        # Extract the numbers from inside the brackets
        # We split by comma and filter out empty strings
        ints_str = ints_match.group(1)
        ints = [int(num) for num in ints_str.split(',') if num]
        
        return p, ints

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        exit(1)
    except Exception as e:
        print(f"Error parsing file: {e}")
        exit(1)

def solve():
    # --- Step 1: Parse the data ---
    print(f"Reading data from {FILENAME}...")
    p, ints = parse_challenge_file(FILENAME)
    print(f"Loaded prime p (first 20 digits): {str(p)[:20]}...")
    print(f"Loaded {len(ints)} integers.")
    print("-" * 40)

    # --- Step 2: Find the Quadratic Residue ---
    # Legendre Symbol: (a / p) = a^((p-1)/2) mod p
    # If result == 1, a is a quadratic residue.
    # If result == p-1 (which is -1), it is not.
    
    quadratic_residue = None
    
    for val in ints:
        legendre_symbol = pow(val, (p - 1) // 2, p)
        
        if legendre_symbol == 1:
            quadratic_residue = val
            print(f">> Found Quadratic Residue: {str(val)[:20]}...")
            break
            
    if quadratic_residue is None:
        print("No quadratic residue found in the list.")
        return

    # --- Step 3: Calculate the Square Root ---
    # The problem implies p = 3 mod 4. Let's verify.
    if p % 4 == 3:
        print("Confirmed: p is congruent to 3 mod 4.")
        print("Using the formula: x = a^((p+1)/4) mod p")
        
        # Formula for square root when p = 3 mod 4
        # sqrt(a) = a^((p+1)/4) mod p
        exponent = (p + 1) // 4
        root1 = pow(quadratic_residue, exponent, p)
        
        # The other root is always p - root1
        root2 = p - root1
        
        # Verify the result
        if pow(root1, 2, p) == quadratic_residue:
            print("Verification Successful: root^2 == val (mod p)")
        
        print("-" * 40)
        print(f"Root 1: {root1}")
        print(f"Root 2: {root2}")
        print("-" * 40)
        
        # The flag is the larger root
        flag = max(root1, root2)
        print("FLAG (The larger root):")
        print(flag)
        
    else:
        print("p is NOT 3 mod 4. This script requires the Tonelli-Shanks algorithm.")

if __name__ == "__main__":
    solve()
