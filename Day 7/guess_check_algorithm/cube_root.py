"""
Cube Root Approximation

This script approximates the cube root of a given number using the guess and check method.
"""

def cube_root(number):
    guess = 0.0  # Start with an initial guess
    tolerance = 0.01  # Acceptable error margin

    while abs(guess**3 - number) > tolerance:  # Check if the guess is close enough
        guess += 0.01  # Increment the guess in small steps

    return guess

# Test the cube_root function
if __name__ == "__main__":
    number = 27
    approx_cube_root = cube_root(number)
    print(f"The approximate cube root of {number} is {approx_cube_root:.2f}")
