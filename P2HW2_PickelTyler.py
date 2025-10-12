# Tyler Pickel
# 2025-10-12
# P2HW2 - List & Grades Summary
# Collect six module grades, then display lowest, highest, sum, and average.

"""
Pseudocode (no repetition/conditionals):
- Prompt user for Module 1..6 grades and store in variables.
- Create a list from those six variables.
- Compute min, max, sum, and average from the list.
- Print a formatted results table (average to two decimals).
"""

# ---- Inputs (no loops) ----
m1 = float(input("Enter grade for Module 1: "))
m2 = float(input("Enter grade for Module 2: "))
m3 = float(input("Enter grade for Module 3: "))
m4 = float(input("Enter grade for Module 4: "))
m5 = float(input("Enter grade for Module 5: "))
m6 = float(input("Enter grade for Module 6: "))

grades = [m1, m2, m3, m4, m5, m6]

# ---- Calculations ----
low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / 6

# ---- Output ----
print("\n------------Results------------")
label_w, val_w = 17, 8
print(f"{'Lowest Grade:':<{label_w}}{low:>{val_w}.1f}")
print(f"{'Highest Grade:':<{label_w}}{high:>{val_w}.1f}")
print(f"{'Sum of Grades:':<{label_w}}{total:>{val_w}.1f}")
print(f"{'Average:':<{label_w}}{avg:>{val_w}.2f}")
print("-" * 44)
