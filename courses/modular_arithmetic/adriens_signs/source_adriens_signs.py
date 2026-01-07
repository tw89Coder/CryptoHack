import re

FILENAME = "output_adriens_signs.txt"

# Encryption parameters from source.py
a = 288260533169915
p = 1007621497415251

def parse_file(filename):
    """
    Robust parser to extract the ciphertext list from the file.
    """
    try:
        with open(filename, 'r') as f:
            content = f.read()
        
        # Clean up: remove newlines and whitespace
        clean_content = "".join(content.split())
        
        # Extract the list content inside brackets
        # Matches strictly for a list of numbers separated by commas
        match = re.search(r'\[([\d,]+)\]', clean_content)
        
        if not match:
            raise ValueError("Could not find ciphertext list in the file.")
            
        # Split by comma and convert to integers
        ciphertext = [int(x) for x in match.group(1).split(',')]
        return ciphertext

    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        exit(1)

def legendre_symbol(n, p):
    """
    Computes Legendre Symbol (n/p)
    Returns:
        1  if n is a Quadratic Residue (QR)
        -1 if n is a Quadratic Non-Residue (QNR) (represented as p-1)
        0  if n is a multiple of p
    """
    return pow(n, (p - 1) // 2, p)

def solve():
    print(f"Checking parameters...")
    # 1. Verify that 'a' is a Quadratic Residue
    if legendre_symbol(a, p) == 1:
        print(f"Confirmed: 'a' is a Quadratic Residue mod p.")
    else:
        print(f"Warning: 'a' is NOT a Quadratic Residue. The logic might be inverted.")

    # 2. Verify p = 3 mod 4 (implies -1 is a non-residue)
    if p % 4 == 3:
        print(f"Confirmed: p = 3 mod 4. (-1 is a Non-Residue).")
    
    print("-" * 40)
    print("Parsing ciphertext...")
    ciphertext = parse_file(FILENAME)
    print(f"Loaded {len(ciphertext)} integers.")
    
    # 3. Decrypt
    # Logic:
    # If Legendre(c, p) == 1  -> c is QR  -> Original bit was '1'
    # If Legendre(c, p) == -1 -> c is QNR -> Original bit was '0'
    
    binary_string = ""
    
    for c in ciphertext:
        ls = legendre_symbol(c, p)
        
        if ls == 1:
            binary_string += "1"
        elif ls == p - 1: # This is -1 in modular arithmetic
            binary_string += "0"
        else:
            print("Error: Legendre symbol is 0 (multiple of p).")
            
    print(f"Recovered Binary Length: {len(binary_string)} bits")
    
    # 4. Convert Binary to String
    # Group by 8 bits
    flag = ""
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        if len(byte) == 8:
            char_code = int(byte, 2)
            flag += chr(char_code)
            
    print("-" * 40)
    print("FLAG:")
    print(flag)
    print("-" * 40)

if __name__ == "__main__":
    solve()