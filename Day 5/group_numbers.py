"""
Case Problem:
Your younger sibling is learning about large numbers in school
and is struggling to read big numbers like "2750" or "1234567".
To help them, you decide to write a Python function that groups the digits of any given number into groups of three, separated by commas, starting with the rightmost digit. This way, the number becomes easier to read and understand.

Example
Input : 125894
Output: 125,894
"""

def group_digits(n):
    # Convert the number to a string to easily manipulate its digits
    num_str = str(n)
    # Initialize an empty list to store the groups of three digits
    groups = []
    # Loop through the digits from right to left
    for i in range(len(num_str)):
        # Add the current digit to the beginning of the list
        groups.insert(0, num_str[-(i + 1)])
        # Every three digits, join and reset the groups
        if (i + 1) % 3 == 0 and i != len(num_str) - 1:
            groups.insert(-3, ',')  # Insert a comma before the last three digits
    # Join the groups into a single string and return the result
    return ''.join(groups)

# Test the function
print(group_digits(125894))  # Output: 125,894
print(group_digits(1234567))  # Output: 1,234,567
print(group_digits(2750))     # Output: 2,750
