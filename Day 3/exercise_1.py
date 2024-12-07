"""
Check Voting Eligibility
Write a program to check if a person is eligible to vote based on their age:
– If age >= 18, print "Eligible to vote."
– Otherwise, print "Not eligible to vote."
"""
# Get the age from the user
age = int(input("Enter your age: "))

# Check if the age is 18 or above
if age >= 18:
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")