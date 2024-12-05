"""
Area and Perimeter of a Rectangle
1. Get the user to input the length and width of the rectangle
"""
# Get the length and width from the user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

"""
2. Calculate the area and perimeter of the rectangle and print the results
"""
# Calculate the area and perimeter
area = length * width

perimeter = 2 * (length + width)

# Results
print(f"The area of the rectangle is: {area} square units")
print(f"The perimeter of the rectangle is: {perimeter} units")