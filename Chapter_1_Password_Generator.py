import random
import string

def generate_password(length, use_digits=True, use_uppercase=True, use_lowercase=True, use_symbols=True):
    char_set = ''
    if use_digits:
        char_set += string.digits
    if use_uppercase:
        char_set += string.ascii_uppercase
    if use_lowercase:
        char_set += string.ascii_lowercase
    if use_symbols:
        char_set += string.punctuation
    if char_set == '':
        raise ValueError("At least one character type must be selected")
    
    password = ''.join(random.choice(char_set) for _ in range(length))
    return password

def main():
    length = int(input("Enter the desired password length: "))
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'
    
    try:
        password = generate_password(length, use_digits, use_uppercase, use_lowercase, use_symbols)
        print(f"Your generated password is: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()