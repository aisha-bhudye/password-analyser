"""
ai_llm_integration.py
----------------------------------------------------------
Adds LLM functionality to the Password Strength Analyser.

Features:
1. LLM explanation of password weaknesses
2. LLM pattern detection (keyboard walks, dictionary-like patterns, etc.)
3. LLM strong password generation
4. Safe, local-only use via Ollama (smollm2:1.7b or any model installed)
----------------------------------------------------------
"""

from ollama import chat


MODEL_NAME = "smollm2:1.7b"   



# 1. LLM EXPLAINS WHY A PASSWORD IS WEAK/STRONG
def llm_explain_password(password: str) -> str:
    """
    Uses the local LLM to produce a safe explanation of password quality.
    """
    prompt = f"""
    You are a cybersecurity assistant. Analyse the password: "{password}".

    Provide a short and safe explanation describing:
    - Why this password might be weak or strong
    - Security risks (if any)
    - DO NOT give dangerous advice.
    - DO NOT output the password again in full.
    """

    response = chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.message.content.strip()



# 2. LLM DETECTS PATTERNS ATTACKERS EXPLOIT
def llm_detect_patterns(password: str) -> str:
    """
    Asks the LLM to identify patterns like:
    - keyboard walks (qwerty, asdf, 12345)
    - leetspeak (p@ssw0rd)
    - repeated characters
    - dictionary-like words
    """

    prompt = f"""
    Analyse the password: "{password}".
    Tell me ONLY what attacker-exploitable patterns you detect.
    Examples: keyboard walks, repetitions, dictionary-like words,
    predictable substitutions, dates, names, etc.
    Keep the response short and factual.
    """

    response = chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.message.content.strip()


# 3. LLM GENERATES A STRONG PASSWORD
def llm_generate_password(length: int = 16) -> str:
    """
    Uses the LLM to generate a strong password.
    Ensures:
    - 16–20 characters (if user requests, it adjusts safely)
    - upper/lowercase
    - numbers
    - symbols
    """

    length = max(12, min(32, length))  # Enforce safe range

    prompt = f"""
    Generate a strong password around {length} characters that includes:
    - upper and lowercase letters
    - numbers
    - symbols

    Requirements:
    - MUST NOT contain dictionary words
    - MUST NOT include personal data
    - Output ONLY the password with no explanation.
    """

    response = chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )

    pwd = response.message.content.strip()

    # strip whitespace and quotes
    return pwd.replace('"', "").replace(" ", "").strip()


#  DEMO MENU FOR TESTING THE LLM MODULE
def demo():
    print("\n=== AI LLM MODULE DEMO ===")
    print("1. Explain a password")
    print("2. Detect patterns")
    print("3. Generate strong password")
    print("4. Exit")

    while True:
        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            pwd = input("Enter password: ")
            print("\n--- AI Explanation ---")
            print(llm_explain_password(pwd))

        elif choice == "2":
            pwd = input("Enter password: ")
            print("\n--- AI Pattern Detection ---")
            print(llm_detect_patterns(pwd))

        elif choice == "3":
            length = input("Password length (default 16): ").strip()
            length = int(length) if length.isdigit() else 16
            print("\n--- AI Strong Password ---")
            print(llm_generate_password(length))

        elif choice == "4":
            print("Goodbye!")
            return

        else:
            print("Invalid choice.")



# Run demo when executed directly
if __name__ == "__main__":
    demo()
