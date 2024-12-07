"""
Find the Largest Number
Write a program that takes three numbers as input and prints the largest of the 
three.
"""
# Get three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the last number: "))

# Find the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Print the largest number
print("The largest number is: ", largest)