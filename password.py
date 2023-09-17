import random
import string

def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_chars=True):
    # Define character sets based on user preferences
    lowercase_letters = string.ascii_lowercase if use_lowercase else ''
    uppercase_letters = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special_characters = '!@#$%^&*()_-+=<>?/[]{}|' if use_special_chars else ''

    # Combine character sets to create the full character pool
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    if not all_characters:
        raise ValueError("Please select at least one character type for the password.")

    # Generate a random password using the full character pool
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

# User-defined preferences for password complexity
length = int(input("Enter the desired password length: "))
use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

# Generate the password based on user preferences
try:
    password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars)
    print("Generated Password:", password)
except ValueError as e:
    print(e)
