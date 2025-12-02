import os


def enumerate_files():
    print("SECTION 2: FILE ENUMERATION")
    print("Searching for authentication system files...\n")

    target_files = [
        'main.py', 'password_checker.py', 'auth_utils.py',
        'user_system.py', 'users.json', 'common_passwords.txt'
    ]

    found_files = {}

    for filename in target_files:
        if os.path.exists(filename):
            size = os.path.getsize(filename)
            found_files[filename] = size
            print(f" FOUND: {filename} ({size} bytes)")
        else:
            print(f" NOT FOUND: {filename}")

    print(f"\nEnumeration complete: {len(found_files)} file(s) discovered")
    return found_files
