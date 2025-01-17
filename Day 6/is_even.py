def is_even(number):
    """
    Check if a number is even.

    Parameters:
    number (int): The number to check.

    Returns:
    bool: True if the number is even, False otherwise.
    """
    return number % 2 == 0

# Test the function
if __name__ == "__main__":
    print(is_even(4))  # True
    print(is_even(7))  # False
