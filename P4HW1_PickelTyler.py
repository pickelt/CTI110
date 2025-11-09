# Tyler Pickel
# Date: 11/9/2025
# P4HW1 - Scores with validation, drop lowest, average, letter grade
# Description: collect N scores (0..100), drop the lowest, show list, average (2 d.p.), and letter grade.

"""
Pseudocode
- Ask how many scores.
- Loop i from 1..N: get score i; while score invalid -> show error and ask again; append to list.
- Find lowest; build a new list without the first lowest.
- Loop to total the modified list; average = total / count.
- Decide letter grade; print results exactly like sample.
"""

# Ask how many
how_many = int(input("How many scores do you want to enter? "))

# Collect with validation
scores = []
i = 1
while i <= how_many:
    # first prompt has a blank line before it (to match screenshot)
    if i == 1:
        value = float(input("\nEnter score #" + str(i) + ": "))
    else:
        value = float(input("Enter score #" + str(i) + ": "))

    # validate 0..100
    while value < 0 or value > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        value = float(input("Enter score #" + str(i) + " again: "))

    scores.append(value)
    i = i + 1

# Lowest
lowest = min(scores)

# Modified list (drop first occurrence of lowest) — no slicing/copy tricks
modified_scores = []
dropped = False
for s in scores:
    if s == lowest and not dropped:
        dropped = True      # skip this one
    else:
        modified_scores.append(s)

# Average using a loop (no sum())
total = 0.0
count = 0
for s in modified_scores:
    total += s
    count += 1
if count > 0:
    average = total / count
else:
    average = 0.0

# Letter grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Results block with same spacing/format as screenshots
print("\n\n-------------Results------------")
print("Lowest Score  : ", lowest)
print("Modified List : ", modified_scores)
print("Scores Average: ", format(average, ".2f"))
print("Grade         : ", grade)
print("---------------------------------")
