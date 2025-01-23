def demonstrate_precision_errors():
    """
    Demonstrate the effect of precision errors in floating-point arithmetic.
    """
    print("Demonstrating precision errors:")
    print("0.1 + 0.2 == 0.3:", 0.1 + 0.2 == 0.3)  # Output: False
    print("0.1 + 0.2:", 0.1 + 0.2)  # Output: 0.30000000000000004

if __name__ == "__main__":
    demonstrate_precision_errors()
