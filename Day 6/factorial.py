def factorial(n):
    """
    Calculate the factorial of a number.

    Parameters:
    n (int): The number to calculate the factorial for.

    Returns:
    int: The factorial of the number.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Test the function
if __name__ == "__main__":
    print(factorial(5))  # 120
