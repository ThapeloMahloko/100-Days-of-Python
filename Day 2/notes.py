"""
Day 2: Python Basics – Notes and Exercises

1. Input and Output in Python


Taking user input using the input() function.
The input is returned as a string.
"""
name = input("Enter your name: ")
# Using f-string to format the output message.
print(f"Hello, {name}!")

# Taking age as input and converting it to an integer using int().
age = int(input("Enter your age: "))
# Displaying the age next year using f-string for formatting.
print(f"Next year, you will be {age + 1} years old.")

# Output example using a predefined age variable.
age = 24
# Using f-string to print the age.
print(f"I am {age} years old.")
# Using .format() method to print the age.
print("I am {} years old.".format(age))

# 2. Basic String Operations
# Concatenation: Combining first and last names.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
# Concatenating first and last names with a space in between.
full_name = first_name + " " + last_name
# Printing the full name.
print(f"Full name: {full_name}")

# Repetition: Printing a string multiple times.
print("Python! " * 3)  # This will print "Python! " three times.

# Indexing: Accessing specific characters in a string.
word = input("Enter a word: ")
# Printing the first character of the word.
print(f"First character: {word[0]}")
# Printing the last character of the word using negative indexing.
print(f"Last character: {word[-1]}")
# Printing the middle character if the word has more than 2 characters.
if len(word) > 2:
    print(f"Middle character: {word[len(word) // 2]}")

# Slicing: Extracting substrings from a string.
quote = input("Enter a quote: ")
# Printing the first 5 characters of the quote.
print(f"First 5 characters: {quote[:5]}")
# Printing the last 5 characters of the quote.
print(f"Last 5 characters: {quote[-5:]}")
# Printing a slice of the quote from index 3 to 8.
print(f"Slice from index 3 to 8: {quote[3:8]}")

# 3. String Methods
# Input a string and demonstrate various string methods.
input_string = input("Enter a string: ")
# Converting the string to uppercase.
print(f"Uppercase: {input_string.upper()}")
# Converting the string to lowercase.
print(f"Lowercase: {input_string.lower()}")
# Trimming whitespace from both ends of the string.
print(f"Trimmed: '{input_string.strip()}'")
# Printing the length of the string.
print(f"Length: {len(input_string)}")

