# Tyler Pickel
# P4LAB2 - Multiplication Table with Loops
# This program asks the user for an integer.
# If the number is 0 or higher, it shows the multiplication table from 1 to 12.
# If it’s negative, it tells the user negative numbers are not allowed.
# Uses a while loop (for repeating) and a for loop (for the table).

run_again = "yes"

while run_again == "yes":
    user_input = int(input("Enter an integer: "))

    if user_input >= 0:
        for i in range(1, 13):
            print(user_input, "*", i, "=", user_input * i)
    else:
        print("This program does not handle negative numbers.")

    run_again = input("\nWould you like to run the program again? ")
    print()

print("Exiting program...")
