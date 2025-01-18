import random
import string

def display_welcome_message():
    print("=" * 50)
    print("           Welcome to the Password Generator           ")
    print("=" * 50)

def get_password_length():
    while True:
        try:
            length = int(input("\nEnter the desired length of the password (minimum 6): "))
            if length >= 6:
                return length
            else:
                print("Password length should be at least 6 characters. Try again!")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_password_complexity():
    print("\nSelect the complexity level of your password:")
    print("1. Only Letters")
    print("2. Letters and Numbers")
    print("3. Letters, Numbers, and Special Characters")
    
    while True:
        try:
            choice = int(input("Choose complexity level (1-3): "))
            if choice in (1, 2, 3):
                return choice
            else:
                print("Invalid choice! Please select a number between 1 and 3.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def generate_password(length, complexity):
    if complexity == 1:
        characters = string.ascii_letters
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    else:  # complexity == 3
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    display_welcome_message()
    
    while True:
        length = get_password_length()
        complexity = get_password_complexity()
        password = generate_password(length, complexity)
        
        print("\nYour generated password is:")
        print(f"{'*' * 20}\n{password}\n{'*' * 20}")
        
        another = input("\nDo you want to generate another password? (yes/no): ").lower()
        if another not in ("yes", "y"):
            print("\nThank you for using the Password Generator. Stay secure!")
            break

if __name__ == "__main__":
    main()