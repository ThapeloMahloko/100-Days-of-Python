def group_digits(n):
    num_str = str(n)
    result = ""
    count = 0
    
    # Loop through the string of digits in reverse order
    for digit in reversed(num_str):
        if count > 0 and count % 3 == 0:
            result = "," + result  # Add a comma every 3 digits
        result = digit + result  # Add the digit to the result string
        count += 1
    
    return result

# Test the function
print(group_digits(125894))  # Output: 125,894
print(group_digits(1234567))  # Output: 1,234,567
print(group_digits(2750))     # Output: 2,750