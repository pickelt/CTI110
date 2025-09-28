# Tyler Pickel
# Date: 2025-09-28
# Assignment Name: P1HW2
# Description: This program calculates and displays travel expenses.

# Pseudocode:
# 1. Ask user to enter budget
# 2. Ask user to enter travel destination
# 3. Ask user for gas cost
# 4. Ask user for accommodation cost
# 5. Ask user for food cost
# 6. Add expenses
# 7. Subtract expenses from budget
# 8. Display results

print("This program calculates and displays travel expenses\n")

# Get user input
budget = float(input("Enter Budget: "))
destination = input("\nEnter your travel destination: ")
gas = float(input("\nHow much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accomodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Calculate total expenses and remaining balance
total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

# Display results
print("\n------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}")
print(f"\nFuel: {gas}")
print(f"Accomodation: {accommodation}")
print(f"Food: {food}")
print("\nRemaining Balance:", remaining_balance)
