
from common_passwords import load_common_passwords
from password_checker import analyse_password
from password_generator import generate_password_menu
from user_system import register_user, authenticate_user

def main():
    print("PASSWORD SECURITY SYSTEM")
    common_passwords = load_common_passwords()

    while True:
        print("\nMain Menu:")
        print("1. Check a password")
        print("2. Generate a new password")
        print("3. Register a new user")
        print("4. Login")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            password = input("\nEnter a password to check: ").strip()
            if password != "":
                analyse_password(password, common_passwords)
            else:
                print("Password cannot be empty.")
        elif choice == "2":
            generate_password_menu(common_passwords)
        elif choice == "3":
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            register_user(username, password)
        elif choice == "4":
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            token = input("Enter TOTP token: ").strip()
            authenticate_user(username, password, token)
        elif choice == "5":
            print("\nThanks for using Password Security System!")
            break
        else:
            print("Invalid option, please enter 1-5.")

if __name__ == "__main__":
    main()
