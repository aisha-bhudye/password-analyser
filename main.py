
from common_passwords import load_common_passwords
from password_checker import analyse_password
from password_generator import generate_password_menu
from user_system import register_user, authenticate_user

# === IMPORT AI MODULE ===
from ai_llm_integration import (
    llm_explain_password,
    llm_detect_patterns,
    llm_generate_password
)

# === IMPORT DECRYPTION MODULE ===
from secure_logging import decrypt_log   

def main():
    print("PASSWORD SECURITY SYSTEM")
    common_passwords = load_common_passwords()

    while True:
        print("\nMain Menu:")
        print("1. Check a password")
        print("2. Generate a new password")
        print("3. Register a new user")
        print("4. Login")
        print("5. AI Tools (LLM Features)")
        print("6. Decrypt Secure Log")        
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ").strip()

        # 1. Password analysis
        if choice == "1":
            password = input("\nEnter a password to check: ").strip()

            if password != "":
                analyse_password(password, common_passwords)

                print("\n--- AI Explanation ---")
                print(llm_explain_password(password))

                print("\n--- AI Pattern Detection ---")
                print(llm_detect_patterns(password))

            else:
                print("Password cannot be empty.")

        # 2. Password generator menu
        elif choice == "2":
            generate_password_menu(common_passwords)

        # 3. Register user
        elif choice == "3":
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            register_user(username, password)

        # 4. Login
        elif choice == "4":
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            token = input("Enter TOTP token: ").strip()
            authenticate_user(username, password, token)

        # 5. AI Tools
        elif choice == "5":
            print("\n=== AI TOOLS MENU ===")
            print("1. AI Explain a password")
            print("2. AI Detect password patterns")
            print("3. AI Generate strong password")
            print("4. Back to main menu")

            ai_choice = input("\nChoose (1-4): ").strip()

            if ai_choice == "1":
                pwd = input("Enter password: ").strip()
                print("\n--- AI Explanation ---")
                print(llm_explain_password(pwd))

            elif ai_choice == "2":
                pwd = input("Enter password: ").strip()
                print("\n--- AI Pattern Detection ---")
                print(llm_detect_patterns(pwd))

            elif ai_choice == "3":
                length = input("Password length (default 16): ").strip()
                length = int(length) if length.isdigit() else 16
                print("\n--- AI-Generated Strong Password ---")
                print(llm_generate_password(length))

            else:
                print("Returning to main menu...")

        # 6. Decrypt a secure encrypted log
        elif choice == "6":
            filename = input("Enter encrypted log filename: ").strip()

            try:
                text = decrypt_log(filename)
                print("\n=== DECRYPTED LOG CONTENT ===")
                print(text)
            except Exception as e:
                print(" Error decrypting file:", e)

        # 7. Exit
        elif choice == "7":
            print("\nThanks for using Password Security System!")
            break

        else:
            print("Invalid option, please enter 1-7.")


if __name__ == "__main__":
    main()
