
import os

def load_common_passwords(filename="common_passwords.txt"):
    common_passwords = set()
    if not os.path.exists(filename):
        print("\nCommon password list not found. Skipping this check.")
        return common_passwords
    with open(filename, "r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            password = line.strip().lower()
            if password != "":
                common_passwords.add(password)
    print(f"\nLoaded {len(common_passwords)} common passwords for checking.\n")
    return common_passwords

def is_common_password(password, common_passwords):
    password_lower = password.lower()
    if password_lower in common_passwords:
        return True
    stripped = "".join([c for c in password_lower if not c.isdigit()])
    return stripped in common_passwords
