"""
Temparature conversion from Celsius to Fahrenheit
"""
# Get the temperature in Celsius from the user
celsius = float(input("Enter the temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Display the result
print(f"The temperature in Fahrenheit is {fahrenheit:.2f}°F")  