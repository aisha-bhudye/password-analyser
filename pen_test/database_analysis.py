import os
import json


def analyze_database():
    print("SECTION 3: DATABASE ANALYSIS")

    if not os.path.exists('users.json'):
        print(" users.json not found")
        print(" No user accounts to analyze")
        return None

    print(" Database file found: users.json\n")

    try:
        with open('users.json', 'r') as f:
            users = json.load(f)

        print(f"Number of accounts: {len(users)}")
        print(f"Usernames found: {list(users.keys())}\n")

        for username, user_data in users.items():
            print(f"User: {username}")

            password_hash = user_data.get('password', '')
            if password_hash.startswith('$2b$'):
                print("  Password Hash: bcrypt  SECURE")
            else:
                print("  Password Hash: WEAK or UNKNOWN")

            if 'secret' in user_data:
                print("  2FA (TOTP): ENABLED")
            else:
                print("  2FA (TOTP): DISABLED")

            print()

        print(" Database analysis complete")
        return users

    except Exception as e:
        print(f" Error reading database: {e}")
        return None
