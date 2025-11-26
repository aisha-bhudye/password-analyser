
import bcrypt, os
PEPPER = os.getenv("PEPPER", "mysecretpepper")

def hash_password(password):
    salted = password + PEPPER
    return bcrypt.hashpw(salted.encode(), bcrypt.gensalt()).decode()

def verify_password(password, hashed):
    salted = password + PEPPER
    return bcrypt.checkpw(salted.encode(), hashed.encode())
