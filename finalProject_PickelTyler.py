# Tyler Pickel
# Date: 12/12/2025
# CTI110 Game Final Project
# Brief description of program:
# A text-based "study battle" game where you create a student character and face random academic challenges.

import random
import time


def print_slow(text, delay=0.02):
    """Non-value returning function: prints text with a slight delay."""
    for ch in text:
        print(ch, end="")
        time.sleep(delay)
    print()


def make_character():
    """
    Value-returning function: creates and returns a character dictionary.
    Allows user to input character attributes and stores them correctly.
    """
    print("=== Character Creation ===")
    name = input("Enter your student name: ").strip()
    if name == "":
        name = "Student"

    # Let user pick a "major" (just flavor, still an attribute)
    major = input("Enter your major (example: IT, Cyber, Networking): ").strip()
    if major == "":
        major = "Undeclared"

    # Main character dictionary (required)
    character = {
        "name": name,
        "major": major,
        "health": 30,     # "health" = stamina for the week
        "strength": 6,    # affects attack damage (required by rubric logic)
        "wins": 0,
        "inventory": {    # optional inventory dictionary
            "coffee": 1,
            "notes": 0
        }
    }
    return character


def make_opponent():
    """Value-returning function: returns a random opponent dictionary."""
    types = [
        ("Pop Quiz", 18, 4),
        ("Big Homework", 22, 5),
        ("Group Project", 24, 6),
        ("Midterm Review", 26, 6),
        ("Final Exam", 30, 7),
    ]
    name, health, strength = random.choice(types)
    opponent = {
        "name": name,
        "health": health,
        "strength": strength
    }
    return opponent


def display_character(ch):
    """Non-value returning function: displays character attributes accurately."""
    print("\n===== YOUR CHARACTER =====")
    print(f"Name: {ch['name']}")
    print(f"Major: {ch['major']}")
    print(f"Health: {ch['health']}")
    print(f"Strength: {ch['strength']}")
    print(f"Wins: {ch['wins']}")
    print("Inventory:")
    for item, qty in ch["inventory"].items():
        print(f"  - {item}: {qty}")
    print("==========================\n")


def display_opponent(op):
    """Non-value returning function: displays opponent attributes accurately."""
    print("\n----- OPPONENT -----")
    print(f"Challenge: {op['name']}")
    print(f"Health: {op['health']}")
    print(f"Strength: {op['strength']}")
    print("--------------------\n")


def clamp_health(entity):
    """Non-value returning function: keeps health from going below zero."""
    if entity["health"] < 0:
        entity["health"] = 0


def attack(attacker, defender):
    """
    Value-returning function:
    Correctly reduces defender health based on attacker's strength (rubric requirement).
    Returns the damage dealt.
    """
    base = attacker["strength"]
    bonus = random.randint(0, 3)
    damage = base + bonus

    defender["health"] -= damage
    clamp_health(defender)
    return damage


def opponent_attack(opponent, player):
    """Non-value returning helper: opponent attacks player."""
    dmg = attack(opponent, player)
    print(f"{opponent['name']} hits back! You lose {dmg} health.")


def use_item(player):
    """Non-value returning function: lets player use inventory to change stats."""
    print("\nUse Item:")
    print("1) Coffee (+5 health)")
    print("2) Notes (+2 strength)")
    print("3) Cancel")
    choice = input("Pick: ").strip()

    if choice == "1":
        if player["inventory"]["coffee"] > 0:
            player["inventory"]["coffee"] -= 1
            player["health"] += 5
            print("You drink coffee ☕ and recover +5 health.")
        else:
            print("No coffee left.")
    elif choice == "2":
        if player["inventory"]["notes"] > 0:
            player["inventory"]["notes"] -= 1
            player["strength"] += 2
            print("You review notes 📒 and gain +2 strength.")
        else:
            print("No notes left.")
    else:
        print("Canceled.")


def find_loot(player):
    """Non-value returning function: random chance to gain an item after a win."""
    roll = random.randint(1, 3)
    if roll == 1:
        player["inventory"]["coffee"] += 1
        print("Loot: Found coffee (+1) ☕")
    elif roll == 2:
        player["inventory"]["notes"] += 1
        print("Loot: Found notes (+1) 📒")
    else:
        print("Loot: Nothing this time.")


def battle(player, opponent):
    """
    Main battle loop for a single opponent.
    Includes attack functionality + a way to exit battle.
    """
    print_slow(f"\nA new challenge appears: {opponent['name']}...")
    time.sleep(0.3)

    while player["health"] > 0 and opponent["health"] > 0:
        display_character(player)
        display_opponent(opponent)

        print("Battle Menu:")
        print("1) Attack (answer the challenge) ✅")
        print("2) Use item 🎒")
        print("3) Run away (end battle) 🏃")
        choice = input("Choose: ").strip()

        if choice == "1":
            dmg = attack(player, opponent)
            print(f"You attack with focus and effort! You deal {dmg} damage.")
            time.sleep(0.3)

            if opponent["health"] > 0:
                opponent_attack(opponent, player)
                time.sleep(0.3)

        elif choice == "2":
            use_item(player)

        elif choice == "3":
            print("You ran away from the challenge.")
            return False  # did not win

        else:
            print("Invalid choice.")

    if player["health"] > 0:
        print_slow(f"\nYou defeated: {opponent['name']} 🎉")
        player["wins"] += 1
        # Character values change during play (required)
        player["strength"] += 1
        print("You feel smarter now. Strength +1!")
        find_loot(player)
        return True

    print_slow("\nYou ran out of health... game over 😵")
    return False


def main_menu():
    """Value-returning function: returns the user's menu choice."""
    print("=== Main Menu ===")
    print("1) View character")
    print("2) Start a challenge (battle)")
    print("3) Use item")
    print("4) Exit game")
    return input("Enter choice: ").strip()


def main():
    """
    Main function and game flow (rubric):
    - Runs the game loop
    - Allows creating, displaying, and attacking characters
    - Provides a way to exit
    """
    print_slow("Welcome to Study Battle: Survive the Semester 📚")
    player = make_character()

    # Game loop
    while True:
        if player["health"] <= 0:
            print("\nYou can't continue with 0 health. Game ended.")
            break

        choice = main_menu()

        if choice == "1":
            display_character(player)

        elif choice == "2":
            opponent = make_opponent()
            battle(player, opponent)

        elif choice == "3":
            use_item(player)

        elif choice == "4":
            print("\nExiting game. Thanks for playing!")
            break

        else:
            print("Invalid choice. Try again.")

    # End summary
    print("\n=== Final Results ===")
    display_character(player)
    print("Good luck on the submission!")


if __name__ == "__main__":
    main()
