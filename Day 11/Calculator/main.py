from art import logo
from calculator import add, subtract, multiply, divide


def calculator():
    print(logo)
    print("Welcome to the Calculator Program:")
    new_calculation = True
    calculator_running = "yes"
    result = 0
    while True:
        if new_calculation:
            num1 = float(input("Enter the first number: "))
        else:
            num1 = result
        print("Select an operation:")
        print("+ : Addition")
        print("- : Subtraction")
        print("* : Multiplication")
        print("/ : Division")
        operation = input("Enter the operation you want to perform: ")
        num2 = float(input("Enter the second number: "))

        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)
        else:
            result = "Invalid operation selected."
        
        print(f"The result of {num1} {operation} {num2} is: {result}")
        calculator_running = input("Do you want to perform another calculation? (yes/no): ").lower()
        
        if calculator_running == "no":
            print("Thank you for using the Calculator Program!")
            break
        new_calculation = input("Do you want to start a new calculation? (yes/no): ").lower() == "yes"


if __name__ == "__main__":
    calculator()