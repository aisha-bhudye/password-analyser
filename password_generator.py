
import string, random
from password_checker import analyse_password

def generate_random_password(length=16):
    length = max(8, min(length, 32))
    chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|"
    return "".join(random.choice(chars) for _ in range(length))

def generate_password_menu(common_passwords):
    print("\nPASSWORD GENERATOR")
    choice = input("1. Random password\n2. Go back\nEnter choice: ").strip()
    if choice == "1":
        length = input("Enter length (default 16): ").strip()
        length = int(length) if length.isdigit() else 16
        password = generate_random_password(length)
        print("\nYour new password:", password)
        analyse_password(password, common_passwords)
