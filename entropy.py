import math


def calculate_entropy(password):
    """
    Calculate password entropy in bits.
    
    Entropy measures the randomness/unpredictability of a password.
    Higher entropy = harder to crack with brute force.
    
    Formula: Entropy = length × log₂(pool_size)
    
    Args:
        password: The password to analyze
    
    Returns:
        float: Entropy in bits (rounded to 2 decimal places)
    """
    pool = 0
    
    # Count character set sizes used
    if any(c.islower() for c in password):
        pool += 26  # lowercase letters
    if any(c.isupper() for c in password):
        pool += 26  # uppercase letters
    if any(c.isdigit() for c in password):
        pool += 10  # digits
    if any(c in "!@#$%^&*()_+-=[]{}|" for c in password):
        pool += 32  # special characters (adjusted to match your symbols)
    
    # Handle edge case: no recognizable characters
    if pool == 0:
        return 0
    
    # Calculate entropy
    entropy = len(password) * math.log2(pool)
    return round(entropy, 2)


def interpret_entropy(entropy):
    """
    Provide human-readable interpretation of entropy value.
    
    Args:
        entropy: Entropy value in bits
    
    Returns:
        tuple: (strength_label, explanation)
    """
    if entropy < 28:
        return "Very Weak 🔴", "Easily cracked in seconds"
    elif entropy < 36:
        return "Weak 🟠", "Could be cracked in minutes to hours"
    elif entropy < 60:
        return "Moderate 🟡", "Would take days to months to crack"
    elif entropy < 80:
        return "Strong 🟢", "Would take years to crack"
    else:
        return "Very Strong 💪", "Would take centuries+ to crack"