def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.

    Parameters:
    fahrenheit (float): The temperature in Fahrenheit.

    Returns:
    float: The temperature in Celsius.
    """
    return (5/9) * (fahrenheit - 32)

# Test the function
if __name__ == "__main__":
    print(convert_to_celsius(98.6))  # 37.0
