import random
import string


def generate_password(length, use_uppercase=True, use_digits=True, use_special_chars=True):
    # Define the character sets to choose from
    char_set = string.ascii_lowercase
    if use_uppercase:
        char_set += string.ascii_uppercase
    if use_digits:
        char_set += string.digits
    if use_special_chars:
        char_set += string.punctuation
          
    # Generate the password
    password = ''.join(random.choice(char_set) for _ in range(length))
    return password


def main():
    print("Password Generator")  
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

        password = generate_password(length, use_uppercase, use_digits, use_special_chars)
        print(f"Generated Password: {password}")

        another = input("Generate another password? (y/n): ").lower()
        if another != 'y':
            break

if __name__ == "__main__":
    main()
