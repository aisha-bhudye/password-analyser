
import json, os
from auth_utils import hash_password, verify_password
from totp_utils import generate_totp_secret, get_qr_code, verify_totp

DB_FILE = "users.json"

def load_users():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(DB_FILE, "w") as f:
        json.dump(users, f)

def register_user(username, password):
    users = load_users()
    if username in users:
        print("User already exists!")
        return
    hashed = hash_password(password)
    secret = generate_totp_secret()
    users[username] = {"password": hashed, "secret": secret}
    save_users(users)
    get_qr_code(secret, username)
    print("User registered successfully! Scan QR for TOTP.")

def authenticate_user(username, password, token):
    users = load_users()
    if username not in users:
        print("User not found!")
        return False
    if not verify_password(password, users[username]["password"]):
        print("Invalid password!")
        return False
    if not verify_totp(token, users[username]["secret"]):
        print("Invalid TOTP token!")
        return False
    print("Login successful!")
    return True
