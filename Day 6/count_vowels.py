def count_vowels(s):
    """
    Count the number of vowels in a given string.

    Parameters:
    s (str): The string to check.

    Returns:
    int: The number of vowels in the string.
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# Test the function
if __name__ == "__main__":
    print(count_vowels("Hello World"))  # 3
