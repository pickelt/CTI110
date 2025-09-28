# Tyler Pickel
# Date: 2025-09-28
# Assignment Name: P1HW1
# Description: Calculate Exponents

print("-----Calculating Exponenets----\n")

base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))

result = base ** exponent
print(f"\n{base} raised to the power of {exponent} is {result} !!\n")

print("-----Addition and Subtraction----\n")

start = int(input("Enter a starting integer: "))
to_add = int(input("Enter an integer to add: "))
to_sub = int(input("Enter an integer to subtract: "))

final_value = start + to_add - to_sub
print(f"\n{start} + {to_add} - {to_sub} is equal to {final_value}")
