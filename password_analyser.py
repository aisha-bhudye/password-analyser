"""
Password Strength Checker
Mini Project - Networks and Systems Security
Author: Aisha Bhudye - 33734353
Date: November 2025
"""
import os
def load_common_passwords(filename="common_passwords.txt"):
    common_passwords = set()

    if not os.path.exists(filename):
        print(f"\n Warning: '{filename}' not found.")
        print("Skipping common password check.\n")
        return common_passwords

    with open(filename, "r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            password = line.strip().lower()
            if password:
                common_passwords.add(password)

    print(f"\nLoaded {len(common_passwords)} common passwords for checking.\n")
    return common_passwords


def is_common_password(password, common_passwords):
    password_lower = password.lower()

    # Exact match
    if password_lower in common_passwords:
        return True

    # Check if removing numbers matches (like Password123 → password)
    stripped = ''.join(ch for ch in password_lower if not ch.isdigit())
    if stripped in common_passwords:
        return True

    return False

def analyse_password(password, common_passwords):
    score = 0
    # Inside analyse_password()
    if is_common_password(password, common_passwords):
        print("This password is too common!")
        print("Hackers often try these first.")
        print("Please choose something unique.\n")
        return
    # 1. Check length
    if len(password) < 8:
        print("Too short! Use at least 8 characters.")
        score += 10
    elif len(password) < 12:
        print(" Length OK, but 12+ characters is better.")
        score += 20
    else:
        print(" Good length!")
        score += 30

    # 2. Check character types
    has_lower = False
    has_upper = False
    has_digit = False
    has_symbol = False

    symbols = "!@#$%^&*()_+-=[]{};:'\",.<>?/\\|`~"

    for character in password:
        if character.islower():
            has_lower = True
        elif character.isupper():
            has_upper = True
        elif character.isdigit():
            has_digit = True
        elif character in symbols:
            has_symbol = True

    if has_lower:
        print("Contains lowercase letters")
        score += 10
    else:
        print("Missing lowercase letters")

    if has_upper:
        print(" Contains uppercase letters")
        score += 10
    else:
        print(" Missing uppercase letters")

    if has_digit:
        print(" Contains numbers")
        score += 10
    else:
        print(" Missing numbers")

    if has_symbol:
        print("Contains special characters")
        score += 15
    else:
        print("Missing special characters")

    # 3. Check for weak patterns 
    weak_words = ["password", "admin", "123", "qwerty", "user"]
    for word in weak_words:
        if word in password.lower():
            print(" Contains common or weak word:", word)
            score -= 25
            break

    # Check for repeating characters (like aaa, 111)
    repeat_found = False
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            repeat_found = True
            break

    if repeat_found:
        print(" Contains repeating characters")
        score -= 10

    # 4. Final strength rating
    if score >= 70:
        strength = "Strong "
    elif score >= 50:
        strength = "Moderate"
    else:
        strength = "Weak"

    print("\nYour password score:", score, "/ 100")
    print(" Strength:", strength)

    # 5. Recommendations
    print("\n Tips to improve:")
    if score < 70:
        print("- Use a mix of uppercase, lowercase, numbers, and symbols.")
        print("- Make it at least 12 characters long.")
        print("- Avoid common words or simple patterns.")
        print("- Try a passphrase (e.g., 'Sunny!Morning@2025')")
    else:
        print(" Great job! Your password looks strong.")
        
    return {"score": score, "strength": strength}



def main():
    print("   PASSWORD STRENGTH CHECKER")
    # Load common passwords file
    common_passwords = load_common_passwords("common_passwords.txt")
    while True:
        print("\n1. Analyze a password")
        print("2. Exit")

        choice = input("\nEnter your choice (1 or 2): ").strip()

        if choice == "1":
            password = input("\nEnter your password: ").strip()
            if password:
                analyse_password(password, common_passwords)
            else:
                print(" Password cannot be empty!")
        elif choice == "2":
            print(f"Common passwords loaded: {len(common_passwords)}")
            print("\nThanks for using Password Strength Checker!")
            break
        else:
            print(" Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
