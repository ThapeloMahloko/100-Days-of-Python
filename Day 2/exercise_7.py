"""
String Formatting: Take user input for name, age and favourite hobby, then 
print a introduction
"""
# Take user input for name, age and favourite hobby
name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your favourite hobby: ")

# Print a introduction
print(f"Hello, my name is {name} and I am {age} years old.\nI love playing {hobby} in my free time.")