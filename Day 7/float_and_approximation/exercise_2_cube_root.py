def cube_root(number):
    """
    Find the cube root of a number using binary search.

    Parameters:
    number (float): The number to find the cube root of.

    Returns:
    float: The approximate cube root.
    """
    low = 0
    high = max(1, number)
    tolerance = 0.01

    while high - low > tolerance:
        mid = (low + high) / 2
        if mid**3 < number:
            low = mid
        else:
            high = mid

    return (low + high) / 2

# Example usage
if __name__ == "__main__":
    print(cube_root(27))  # Output: 3.0
