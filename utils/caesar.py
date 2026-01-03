import enchant
import re
import sys

def caesar_cipher_with_enchant(text):
    # Initialize English dictionary (US English)
    try:
        d = enchant.Dict("en_US")
    except Exception as e:
        print("Error: English dictionary not found.")
        print("Please run: sudo apt install aspell-en")
        return

    # ANSI Escape Codes for coloring
    GREEN = '\033[92m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

    print(f"\nTarget String: '{text}'")
    print("-" * 60)
    
    for shift in range(1, 26):
        # Step 1: Perform Caesar shift on the entire string
        raw_decoded = ""
        for char in text:
            if char.isalpha():
                # Determine if the character is uppercase or lowercase
                base = ord('A') if char.isupper() else ord('a')
                # Apply shift logic
                raw_decoded += chr((ord(char) - base - shift) % 26 + base)
            else:
                # Keep non-alphabetic characters (numbers, symbols) as they are
                raw_decoded += char
        
        # Step 2: Split string while keeping delimiters to colorize specific words
        # Using ([^a-zA-Z]) in parentheses keeps the delimiters in the resulting list
        tokens = re.split(r'([^a-zA-Z])', raw_decoded)
        
        final_line_output = ""
        has_match = False
        
        for token in tokens:
            # Only check alphabetic strings longer than 1 character (to avoid spamming 'a' or 'i')
            if token.isalpha() and len(token) > 1:
                if d.check(token):
                    # Colorize ONLY the valid word
                    final_line_output += f"{GREEN}{BOLD}{token}{RESET}"
                    has_match = True
                else:
                    final_line_output += token
            else:
                final_line_output += token
        
        # Step 3: Print result with a prefix marker if a word was found
        status_marker = f"{GREEN}[+]{RESET} " if has_match else "    "
        print(f"{status_marker}Shift {shift:02d}: {final_line_output}")

if __name__ == "__main__":
    try:
        user_input = input("Enter the string to decode: ").strip()
        if user_input:
            caesar_cipher_with_enchant(user_input)
        else:
            print("Input cannot be empty.")
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()