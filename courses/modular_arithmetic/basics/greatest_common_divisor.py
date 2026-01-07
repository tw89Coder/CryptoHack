def gcd(a, b):
    """
    Computes the Greatest Common Divisor (GCD) of a and b
    using the iterative Euclidean Algorithm.
    """
    
    # Continue the loop as long as b (the divisor/remainder) is not 0.
    while b:
        # Python's simultaneous assignment (Tuple Unpacking).
        # This is a concise way to update values without a temporary variable.
        # Logic:
        # 1. The new 'a' becomes the old 'b'.
        # 2. The new 'b' becomes the remainder of 'a divided by b'.
        #
        # Mathematically, this relies on the property: 
        # gcd(a, b) = gcd(b, a % b)
        a, b = b, a % b

    # When b becomes 0, it means the previous remainder divided evenly.
    # Therefore, 'a' holds the last non-zero remainder, which is the GCD.
    return a

# --- Main Execution ---

a = 66528
b = 52920

result = gcd(a, b)

print(f"a = {a}, b = {b}")
print(f"GCD: {result}")