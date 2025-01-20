"""
Smallest Divisible Number

This script finds the smallest number between 1 and 200 that is divisible by 5, 6, and 8.
"""

def find_smallest_divisible():
    for number in range(1, 201):  # Check numbers between 1 and 200
        if number % 5 == 0 and number % 6 == 0 and number % 8 == 0:  # Check divisibility
            return number  # Return the first number found

# Test the find_smallest_divisible function
if __name__ == "__main__":
    smallest_number = find_smallest_divisible()
    print(f"The smallest number between 1 and 200 that is divisible by 5, 6, and 8 is {smallest_number}.")
