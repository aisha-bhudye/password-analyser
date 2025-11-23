from common_passwords import is_common_password
from entropy import calculate_entropy
from entropy import interpret_entropy
def analyse_password(password, common_passwords):
    print("\nChecking your password...\n")

    score = 0

    # 1. Check if password is common
    if is_common_password(password, common_passwords):
        print("This password is too common!")
        print("Hackers often guess these first.")
        return {"score": 0, "strength": "Very Weak"}

    # 2. Check length
    if len(password) < 8:
        print("Too short! Try at least 8 characters.")
        score += 10
    elif len(password) < 12:
        print("OK length, but 12+ is better.")
        score += 20
    else:
        print("Great length!")
        score += 30

    # 3. Check character types
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
        print("Has lowercase letters")
        score += 10
    else:
        print("Missing lowercase letters")

    if has_upper:
        print("Has uppercase letters")
        score += 10
    else:
        print("Missing uppercase letters")

    if has_digit:
        print("Has numbers")
        score += 10
    else:
        print("Missing numbers")

    if has_symbol:
        print("Has special symbols")
        score += 15
    else:
        print("Missing special symbols")

    # 4. Check for weak words or patterns
    weak_words = ["password", "admin", "123", "qwerty", "user"]
    for word in weak_words:
        if word in password.lower():
            print("Contains weak word:", word)
            score -= 25
            break

    # Repeated characters (like "aaa" or "111")
    has_repeat = False
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            has_repeat = True
            break

    if has_repeat:
        print("Has repeating characters")
        score -= 10

    # 5. Rate strength
    if score >= 70:
        strength = "Strong"
    elif score >= 50:
        strength = "Moderate"
    else:
        strength = "Weak"

    print("Password Strength:", strength)
    print("Score:", score, "/ 100")
    
    # Calculate entropy
    entropy = calculate_entropy(password)
    entropy_label, entropy_explanation = interpret_entropy(entropy)

    # Display it
    print(f"\n ENTROPY ANALYSIS:")
    print(f"Entropy: {entropy} bits")
    print(f"Rating: {entropy_label}")
    print(f"Crack Time: {entropy_explanation}")

    # 6. Tips
    if score < 70:
        print("\nTips to improve:")
        print("- Make it at least 12 characters long.")
        print("- Use a mix of upper/lowercase, numbers, and symbols.")
        print("- Avoid common words or repeated letters.")
        print("- Try using a passphrase like 'Sunny!River@2025'.")
    else:
        print("\nExcellent! Your password looks strong and secure.")

    return {"score": score, "strength": strength}


