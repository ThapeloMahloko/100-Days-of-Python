"""
Build a program that will ask bill paid, percentage tip given and how many people will contributes. To 
calculate the amount each person will pay.
"""
print("Will come to the split the bill calculator")

# Get the bill paid
bill_paid = float(input("Enter the bill paid: R"))

# Get the percentage tip given
tip_percentage = float(input("Enter the percentage tip given(e.g 10, 15, 25): "))

# Get the number of people contributing
people_contributing = int(input("Enter the number of people contributing: "))

# Calculate the total bill with tip
total_bill = bill_paid + (bill_paid * (tip_percentage / 100))

# Calculate the amount each person will pay
amount_per_person = total_bill / people_contributing

# Print the result
print(f"Each person will pay: R{round(amount_per_person, 2)}")
