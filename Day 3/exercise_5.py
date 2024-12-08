"""
Triangle Validator
Write a program to check if three given sides can form a valid triangle.
(Hint: The sum of any two sides must be greater than the third side.)
"""
# Get the lengths of the three sides from the user
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Check if the sum of any two sides is greater than the third side
if (side1 < side2 + side3) and (side2 < side1 + side3) and (side3 < side1 + side2):
    print("This is a triangle")
else:
    print("This is not a triangle")