# Tyler Pickel
# 2025-10-12
# P2HW1 - Travel Expenses
# This program collects a trip budget and expected costs, then prints them in a nicely formatted table.

print("This program calculates and displays travel expenses\n")

# ---- Inputs ----
budget = float(input("Enter Budget: "))
destination = input("\nEnter your travel destination: ")

fuel = float(input("\nHow much do you think you will spend on gas? "))
hotel = float(input("Approximately, how much will you need for accomodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# ---- Calculations ----
total_spent = fuel + hotel + food
remaining = budget - total_spent

# ---- Output ----
print("\n------------Travel Expenses------------")
label_w = 18  # width for the left column (labels)
val_w = 14    # width for the right column (values)

print(f"{'Location:':<{label_w}}{destination:>{val_w}}")
print(f"{'Initial Budget:':<{label_w}}${budget:>{val_w-1}.2f}")
print(f"{'Fuel:':<{label_w}}${fuel:>{val_w-1}.2f}")
print(f"{'Accomodation:':<{label_w}}${hotel:>{val_w-1}.2f}")
print(f"{'Food:':<{label_w}}${food:>{val_w-1}.2f}")
print("--------------------------------------")

print(f"\nRemaining Balance:  ${remaining:,.2f}")
