"""
This program will check if the inputed value less than, greater than or equal to 5.
"""

a = int(input("Enter a integer value between 0 to 9:"))

#check condition
if a < 5:
    print("Less than 5")
elif a == 5:
    print("Equal to 5")
else:
    print("Greater than 5")