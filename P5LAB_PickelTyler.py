# Tyler Pickel
# 11/30/2025
# P5LAB
# Self-checkout change calculator using functions and random

import random


def disperse_change(change_amount):
    """Break change into dollars, quarters, dimes, nickels, and pennies."""

    # work in whole cents to avoid float issues
    cents = round(change_amount * 100)

    dollars = cents // 100
    cents = cents % 100

    quarters = cents // 25
    cents = cents % 25

    dimes = cents // 10
    cents = cents % 10

    nickels = cents // 5
    cents = cents % 5

    pennies = cents

    # only print a line if that coin amount is not zero
    if dollars > 0:
        print(dollars, "Dollars")
    if quarters > 0:
        print(quarters, "Quarters")
    if dimes > 0:
        print(dimes, "Dimes")
    if nickels > 0:
        print(nickels, "Nickels")
    if pennies > 0:
        print(pennies, "Pennies")


def main():
    # random total owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${amount_owed:.2f}")

    # ask how much cash they put in
    cash = float(input("How much cash will you put in the self-checkout? "))

    # make sure they put in at least enough (loop requirement)
    while cash < amount_owed:
        print("That is not enough money.")
        cash = float(input("Please enter an amount that is at least what you owe: "))

    # compute change
    change = round(cash - amount_owed, 2)
    print(f"Change is: ${change:.2f}\n")

    # call your previous function
    disperse_change(change)


# call main so the program actually runs
main()
