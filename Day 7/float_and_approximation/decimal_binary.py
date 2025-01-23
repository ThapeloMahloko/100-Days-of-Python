"""
Decimal to Binary converter.
=====================================
This script converts decimal numbers to binary numbers.
"""

def decimal_binary(decimal_num: int):
    binary_num = ""

    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num = str(remainder) + binary_num
        decimal_num = decimal_num // 2

    return binary_num

print(decimal_binary(55))