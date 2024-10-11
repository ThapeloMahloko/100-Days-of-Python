# Modulo operator notes
# The modulo operator returns the remainder of the division of the number before it by the number after it
# It can be used to check if a number is even or odd by using the modulo operator with
# 2. If the remainder is 0, the number is even. If the remainder is
# 1, the number is odd.
# The modulo operator can also be used to check if a number is divisible by another number. 
#For example: 
#   17 % 5 = 2  # 17 divided by 5 leaves a
# remainder of 2
#   20 % 5 = 0  # 20 divided by 5 leaves a
# remainder of 0
#   21 % 5 = 1  # 21 divided by 5 leaves a
# remainder of 1
number_check = int(input("What is th number you want to check? "))
print(number_check % 2)
