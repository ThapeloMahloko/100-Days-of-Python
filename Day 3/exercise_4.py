"""
Discount Calculator
Write a program to calculate a discount based on the purchase amount:
– For amounts >= 500, apply a 20% discount.
– For amounts >= 200 but less than 500, apply a 10% discount.
– Otherwise, no discount
"""
# Get the total purchase amount from the user
amount = float(input("Enter the total purchase amount: "))

# Determine the discount percentage based on the purchase amount
if amount >= 500:
    discount_percentage = 0.20
elif amount >= 200:
    discount_percentage = 0.10
else:
    discount_percentage = 0.00

# Total discount amount
discount_amount = amount * discount_percentage

# Calculate the final amount after discount
final_amount = amount - discount_amount

# Display the results
print(f"The final amount after discount is: R {round(final_amount, 2)}") # Round to 2 decimal places for currency display

