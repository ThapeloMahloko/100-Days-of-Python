"""
Arithmetic Operation with Uers Input

1. Asks the user for two numbers
"""
# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

"""
2. Perform and print the results of the following operations:
"""
# Addition
result_add = num1 + num2
print(f"The sum of {num1} and {num2} is {result_add}")

# Subtraction
result_sub = num1 - num2
print(f"The difference of {num1} and {num2} is {result_sub}")

# Multiplication
result_mul = num1 * num2
print(f"The product of {num1} and {num2} is {result_mul}")

# Division
result_div = num1 / num2
print(f"The quotient of {num1} and {num2} is {result_div}")

# Modulus
result_mod = num1 % num2
print(f"The remainder of {num1} divided by {num2} is {result_mod}")

# Exponentiation
result_exp = num1 ** num2
print(f"The result of {num1} raised to the power of {num2} is {result_exp}")