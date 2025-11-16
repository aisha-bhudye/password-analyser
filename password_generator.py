import string
import random
from password_checker import analyse_password
def generate_random_password(length=16):
    if length < 8:
        length = 8
    elif length > 32:
        length = 32

    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!@#$%^&*()_+-=[]{}|"

    all_characters = letters + numbers + symbols
    password = ""

    for i in range(length):
        random_character = random.choice(all_characters)
        password += random_character

    return password


# Password Generator Menu
def generate_password_menu(common_passwords):
    print("\nPASSWORD GENERATOR")
    print("1. Random password (very strong)")
    print("2. Go back")

    choice = input("\nEnter your choice (1-3): ").strip()

    if choice == "1":
        length = input("Enter length (default 16): ").strip()

        if length.isdigit():
            length = int(length)
        else:
            length = 16

        password = generate_random_password(length)
        print("\nYour new random password:\n")
        print(password)
        analyse_password(password, common_passwords)
    else:
        print("Returning to main menu...")
