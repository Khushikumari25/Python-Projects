import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    # Define character sets based on user preferences
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    # Check if at least one character set is selected
    if not characters:
        print("Error: At least one character set should be selected.")
        return None

    # Generate a random password using the defined characters
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    print("Random Password Generator")

    # Get user input for password length and character sets
    length = int(input("Enter the length of the password: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    # Generate and display the password
    password = generate_password(length, use_uppercase, use_digits, use_special_chars)

    if password:
        print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()