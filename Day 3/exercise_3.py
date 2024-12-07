"""
Odd or Even
Write a program to check if a number is odd or even.
"""
# Get the number from the user
num = int(input("Enter a number: "))

# Check if the number is odd or even
if num % 2 == 0:
    print(f"The number {num} is even.")
else:
    print(f"The number {num} is odd.")
    