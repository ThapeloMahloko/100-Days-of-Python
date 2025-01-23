def approximately_equal(a, b, tolerance=1e-9):
    """
    Check if two floating-point numbers are approximately equal.

    Parameters:
    a (float): First number.
    b (float): Second number.
    tolerance (float): The tolerance for comparison.

    Returns:
    bool: True if approximately equal, False otherwise.
    """
    return abs(a - b) < tolerance

# Example usage
if __name__ == "__main__":
    print(approximately_equal(0.1 + 0.2, 0.3))  # Output: True
