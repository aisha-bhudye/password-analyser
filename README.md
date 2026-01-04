
# Password Strength Analyser & Secure Authentication System

## Project Overview

This project is a **Password Strength Analyser and Secure Authentication System** developed in Python as part of the *Networks and Systems Security* module.

The system helps users to:
- Analyse password strength using industry security standards
- Detect common, weak, and predictable passwords
- Calculate password entropy
- Generate secure random passwords
- Securely store passwords using bcrypt hashing
- Use Two-Factor Authentication (TOTP)
- Demonstrate brute-force and penetration testing concepts
- Encrypt security reports using Hybrid RSA/AES encryption
- Use a **local LLM (Ollama)** for AI-assisted password explanations

No user passwords are stored in plaintext or transmitted externally.  
All processing is performed locally.

---

## Features

- Password length, complexity, pattern, and dictionary analysis
- Common password detection (10,000 password list)
- Shannon entropy calculation with human-readable feedback
- Cryptographically secure password generator
- bcrypt hashing with salt and pepper
- Time-based One-Time Passwords (TOTP)
- Brute-force attack simulation (educational)
- Simple penetration testing utilities
- Hybrid RSA/AES encrypted security logs
- Local AI (LLM) explanations using Ollama

---

## Technology Stack

- **Python**: 3.12+
- **Operating System**: Windows (tested), Linux/macOS supported
- **Development Environment**: Visual Studio Code
- **Version Control**: Git & GitHub
- **Local LLM**: Ollama (`smollm2:1.7b`)

---

## Project Structure

```text
.
├── main.py
├── password_checker.py
├── common_passwords.py
├── entropy.py
├── password_generator.py
├── auth_utils.py
├── totp_utils.py
├── user_system.py
├── brute_force_demo.py
├── ai_llm_integration.py
├── penetration_test.py
├── common_passwords.txt
├── users.json
├── public_key.pem
├── private_key.pem
└── secure_log.json
````

---

## Installation Instructions

### 1. Install Python

Download and install **Python 3.12 or later** from:
[https://www.python.org/downloads/](https://www.python.org/downloads/)

Verify installation:

```bash
python --version
```

---

### 2. Clone the Repository

```bash
git clone https://github.com/aisha-bhudye/password-analyser.git
cd password-analyser
```

---

### 3. Install Required Python Packages

Install dependencies using `pip`:

```bash
pip install bcrypt pyotp qrcode cryptography ollama
```

If you are using Windows and `pip` is not recognised:

```bash
python -m pip install bcrypt pyotp qrcode cryptography ollama
```

---

### 4. Set Environment Variable (Pepper)

The system uses a **pepper** for additional password security.

**Windows (PowerShell):**

```powershell
setx PEPPER "your_secret_pepper"
```

Restart your terminal after setting this variable.

---

### 5. (Optional) Install Ollama for AI Features

Download Ollama:
[https://ollama.com/](https://ollama.com/)

Pull the model used in this project:

```bash
ollama pull smollm2:1.7b
```

>  AI features are optional. The system functions fully without Ollama.

---

## How to Run the Application

Start the program using:

```bash
python main.py
```

You will see a menu with options to:

* Analyse a password
* Generate a secure password
* Register a user
* Log in with 2FA
* Use AI password tools
* Encrypt or decrypt security logs

---

## Ethical Notice

This project is for **educational purposes only**.

All penetration testing, brute-force simulations, and vulnerability demonstrations are performed on systems created and owned by the developer. No real user data is used.

---

## Security Standards Followed

* NIST SP 800-63B
* OWASP Password Storage Cheat Sheet
* RFC 6238 (TOTP)
* Industry best practices for hashing and encryption

---
### AI Declaration

I acknowledge the use of [1] ChatGPT (https://chat.openai.com/) to [2] assist with identifying and debugging errors in my code, clarifying programming concepts, and suggesting improvements to code structure. I entered the following prompts on Accessed:  November 2025 -  Decemeber 2025:

[3] Example prompts used:

“Explain why this error message appears in my code and how to fix it.”

“Suggest a clearer way to structure this function.”

“What is the correct syntax for implementing this feature?”

[4] The output from the generative artificial intelligence was used only to understand errors, explore potential solutions, and improve the organisation of my code. No AI-generated code was copied or included in the final submitted application. All implementation decisions and final code are my own.

## Reference

OpenAI (2025) ChatGPT [Generative AI model]. Available at: https://chat.openai.com/ (Accessed: November 2025 - Decemeber 2025).

---

## Author

**Aisha Bhudye**
Networks and Systems Security
Student ID: 33734353

```


