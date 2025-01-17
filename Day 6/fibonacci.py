def fibonacci(n):
    """
    Calculate the nth Fibonacci number.

    Parameters:
    n (int): The position in the Fibonacci sequence.

    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Test the function
if __name__ == "__main__":
    print(fibonacci(5))  # 5
