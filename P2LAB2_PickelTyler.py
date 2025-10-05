# Tyler Pickel
# October 5, 2025
# P2LAB2
# This program stores vehicle MPG data in a dictionary, allows the user to choose a vehicle,
# and then calculates how many gallons of gas are needed for a given distance.

# Create the dictionary
cars = {
    'Camaro': 18.21,
    'Prius': 52.36,
    'Model S': 110,
    'Silverado': 26
}

# Display the available keys
keys = cars.keys()
print(keys)

# Ask the user to select a vehicle
vehicle = input("\nEnter a vehicle to see its mpg: ")

# Show the MPG of the selected vehicle
mpg = cars[vehicle]
print(f"\nThe {vehicle} gets {mpg} mpg.\n")

# Ask the user for miles they plan to drive
miles = float(input(f"How many miles will you drive the {vehicle}? "))

# Calculate the gallons of gas needed
gallons_needed = miles / mpg

# Display the result rounded to two decimals
print(f"\n{gallons_needed:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles:.1f} miles.")
