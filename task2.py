# Simple Calculator

def display_welcome_message():
    print("=" * 40)
    print("       Welcome to the Simple Calculator       ")
    print("=" * 40)

def display_operations():
    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exponentiation (**)")
    print("7. Floor Division (//)")

def get_user_input():
    while True:
        try:
            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input! Please enter valid numbers.")

def get_operation_choice():
    while True:
        try:
            choice = int(input("Choose an operation (1-7): "))
            if choice in range(1, 8):
                return choice
            else:
                print("Invalid choice! Please select a number between 1 and 7.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def calculate_result(num1, num2, choice):
    operations = {
        1: ("Addition", num1 + num2),
        2: ("Subtraction", num1 - num2),
        3: ("Multiplication", num1 * num2),
        4: ("Division", "Error (Division by zero)" if num2 == 0 else num1 / num2),
        5: ("Modulus", "Error (Division by zero)" if num2 == 0 else num1 % num2),
        6: ("Exponentiation", num1 ** num2),
        7: ("Floor Division", "Error (Division by zero)" if num2 == 0 else num1 // num2)
    }
    return operations[choice]

def display_result(operation, result):
    print(f"\nResult of {operation}: {result}")

def main():
    display_welcome_message()
    while True:
        display_operations()
        num1, num2 = get_user_input()
        choice = get_operation_choice()
        operation, result = calculate_result(num1, num2, choice)
        display_result(operation, result)

        again = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if again not in ("yes", "y"):
            print("\nThank you for using the Simple Calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()