# Tyler Pickel
# Date: 10/19/2025
# P3LAB_Branching
# This program takes a float amount of money and calculates the most efficient
# number of dollars, quarters, dimes, nickels, and pennies needed.
# It uses floor division (//) and subtraction, and omits coins with a value of 0.

amount = float(input("Enter the amount of money as a float: $"))

# Convert to cents to avoid float issues
cents = int(round(amount * 100))

# Calculate each coin value
dollars = cents // 100
cents -= dollars * 100

quarters = cents // 25
cents -= quarters * 25

dimes = cents // 10
cents -= dimes * 10

nickels = cents // 5
cents -= nickels * 5

pennies = cents

# Output results
if dollars == 0 and quarters == 0 and dimes == 0 and nickels == 0 and pennies == 0:
    print("No change")
else:
    if dollars > 0:
        if dollars == 1:
            print(f"{dollars} Dollar")
        else:
            print(f"{dollars} Dollars")
    if quarters > 0:
        if quarters == 1:
            print(f"{quarters} Quarter")
        else:
            print(f"{quarters} Quarters")
    if dimes > 0:
        if dimes == 1:
            print(f"{dimes} Dime")
        else:
            print(f"{dimes} Dimes")
    if nickels > 0:
        if nickels == 1:
            print(f"{nickels} Nickel")
        else:
            print(f"{nickels} Nickels")
    if pennies > 0:
        if pennies == 1:
            print(f"{pennies} Penny")
        else:
            print(f"{pennies} Pennies")
