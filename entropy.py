
import math

def calculate_entropy(password):
    pool = 0
    if any(c.islower() for c in password): pool += 26
    if any(c.isupper() for c in password): pool += 26
    if any(c.isdigit() for c in password): pool += 10
    if any(c in "!@#$%^&*()_+-=[]{}|" for c in password): pool += 32
    if pool == 0: return 0
    return round(len(password) * math.log2(pool), 2)

def interpret_entropy(entropy):
    if entropy < 28: return "Very Weak", "Cracked in seconds"
    elif entropy < 36: return "Weak", "Minutes to hours"
    elif entropy < 60: return "Moderate", "Days to months"
    elif entropy < 80: return "Strong", "Years"
    else: return "Very Strong", "Centuries"
