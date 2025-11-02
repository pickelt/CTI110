# Tyler Pickel
# P4LAB2 - Multiplication table with loops
# Ask for an integer. If it's zero or higher, print the table 1..12.
# If it's negative, tell the user we don't accept negative numbers.
# After each run, ask if the user wants to run again.
# Uses BOTH a while loop (program repeat) and a for loop (table).

def print_table(n: int) -> None:
    # for-loop prints the 1..12 table
    for i in range(1, 13):
        print(f"{n} * {i} = {n * i}")

def main():
    # while-loop to repeat the whole program
    keep_going = True
    while keep_going:
        # read an integer from the user
        try:
            user_input = int(input("Enter an integer: "))
        except ValueError:
            print("Please enter a whole number (no decimals).")
            # go back to the top of the while loop
            # so the user can try again without asking run-again yet
            continue

        if user_input >= 0:
            print()
            print_table(user_input)
            print()
        else:
            print()
            print("This program does not handle negative numbers.")
            print()

        # ask to run again
        answer = input("Would you like to run the program again? ").strip().lower()
        if answer in ("yes", "y"):
            keep_going = True
            print()  # blank line between runs
        else:
            keep_going = False
            print("\nExiting program...")

if __name__ == "__main__":
    main()
