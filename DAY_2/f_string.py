# f-strings are a way to format strings in Python. They are a more readable and efficient
# way to format strings compared to the % operator or the str.format() method.
# The syntax for f-strings is as follows: f"string {variable} string"
# The variable will be replaced with its value in the string.
# For example:
name = "Thapelo"
print(f"Hello, {name}!")  # prints "Hello, John!" if name is
# "John"
# f-strings can also be used to format numbers and other types of variables.
age = 25
print(f"I am {age} years old.")  # prints "I am 25 years old
# f-strings can also be used to format strings with multiple variables.
name = "Thapelo"
age = 25
print(f"Hello, my name is {name} and I am {age} years old.")
# f-strings can also be used to format strings with variables that are lists or
# tuples.
# For example:
fruits = ["apple", "banana", "cherry"]
print(f"My favorite fruits are {fruits}.")  # prints "My favorite fruits are
# ['apple', 'banana', 'cherry']"
# f-strings can also be used to format strings with variables that are dictionaries.
# For example:
person = {"name": "Thapelo", "age": 25}
print(f"My name is {person['name']} and I am {person['age']} years old")
# prints "My name is Thapelo and I am 25 years old"
# f-strings can also be used to format strings with variables that are objects.

