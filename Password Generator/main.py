import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation # Common symbols

    if not characters:
        return "Error: Please select at least one character type."

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("--- Simple Password Generator ---")

    while True:
        try:
            length = int(input("Enter desired password length (e.g., 12): "))
            if length <= 0:
                print("Password length must be a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    use_uppercase = input("Include uppercase letters (A-Z)? (yes/no): ").lower().startswith('y')
    use_lowercase = input("Include lowercase letters (a-z)? (yes/no): ").lower().startswith('y')
    use_digits = input("Include numbers (0-9)? (yes/no): ").lower().startswith('y')
    use_symbols = input("Include symbols (!@#$%^&*)? (yes/no): ").lower().startswith('y')

    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)

    print("\n--- Generated Password ---")
    print(password)
    print("--------------------------")

    input("\nPress Enter to exit.")

if __name__ == "__main__":
    main()
