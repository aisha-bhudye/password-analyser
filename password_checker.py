
from common_passwords import is_common_password
from entropy import calculate_entropy, interpret_entropy
from secure_logging import encrypt_log   

def analyse_password(password, common_passwords):
    print("\nChecking your password...\n")

    score = 0

    # Common password check
    if is_common_password(password, common_passwords):
        print("This password is too common!")
        result = {"score": 0, "strength": "Very Weak"}
    else:
        # Length scoring
        if len(password) < 8:
            print("Too short! Try at least 8 characters.")
            score += 10
        elif len(password) < 12:
            print("OK length, but 12+ is better.")
            score += 20
        else:
            print("Great length!")
            score += 30

        # Character features
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        symbols = "!@#$%^&*()_+-=[]{};:'\",.<>?/\\|`~"
        has_symbol = any(c in symbols for c in password)

        if has_lower: score += 10
        if has_upper: score += 10
        if has_digit: score += 10
        if has_symbol: score += 15

        # Weak substrings
        weak_words = ["password", "admin", "123", "qwerty", "user"]
        for word in weak_words:
            if word in password.lower():
                score -= 25
                break

        # Strength label
        strength = (
            "Strong" if score >= 70
            else "Moderate" if score >= 50
            else "Weak"
        )

        print("Password Strength:", strength)

        entropy = calculate_entropy(password)
        label, explanation = interpret_entropy(entropy)
        print(f"Entropy: {entropy} bits | {label} | {explanation}")

        result = {"score": score, "strength": strength}

    # Offer to ENCRYPT this password analysis
    choice = input("\nEncrypt this password analysis using RSA/AES? (y/n): ").strip().lower()
    if choice == "y":

        # Build a readable report for encryption
        report = f"""
=== SECURE PASSWORD ANALYSIS REPORT ===

Password Entered: {password}
Score: {result["score"]}
Strength: {result["strength"]}
Entropy Label: {label}
Entropy Explanation: {explanation}
"""

        filename = encrypt_log(report)
        print(f"\n Encrypted securely and saved as: {filename}")

    return result
