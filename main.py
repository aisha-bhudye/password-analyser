from common_passwords import load_common_passwords
from password_checker import analyse_password
from password_generator import generate_password_menu

def main():
    print("PASSWORD STRENGTH CHECKER")

    common_passwords = load_common_passwords()

    while True:
        print("\nMain Menu:")
        print("1. Check a password")
        print("2. Generate a new password")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            password = input("\nEnter a password to check: ").strip()
            if password != "":
                analyse_password(password, common_passwords)
            else:
                print("Password cannot be empty.")
        elif choice == "2":
            generate_password_menu(common_passwords)
        elif choice == "3":
            print("\nThanks for using Password Strength Checker!")
            break
        else:
            print("Invalid option, please enter 1, 2, or 3.")


# Run the program
if __name__ == "__main__":
    main()
