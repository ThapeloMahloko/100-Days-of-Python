"""
String Method: Input a string and output uppercase, lowercase, trimmed version and length.
"""
# Get string input from user
user_string = input("Please enter a string: ")

# Convert string to uppercase
uppercase_string = user_string.upper()
print("Uppercase version: ", uppercase_string)

# Convert string to lowecase
lowercase_string = user_string.lower()
print("Lowercase version: ", lowercase_string)

# Trim string (remove leading and trailing whitespace)
trimmed_string = user_string.strip()
print("Trimmed version: ", trimmed_string)

# Get length of string
string_length = len(user_string)
print("Length of string: ", string_length)
