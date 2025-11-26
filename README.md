Here’s the updated **README in Markdown format** for your new system:

***

# **Secure Password Authentication System**

**Mini Project – Networks and Systems Security**  
**Author:** Aisha Bhudye - 33733453  
**Date:** November 2025

***

## **Overview**

This project evolved from a simple password strength checker into a **complete authentication system** that integrates modern security practices:

*   **Password Strength Analysis**
*   **Secure Password Hashing (bcrypt + pepper)**
*   **Two-Factor Authentication (TOTP)**
*   **Brute Force Attack Simulation**
*   **Full Registration & Login Flow**

***

## **Features**

*   **Password Strength Checker:**
    *   Length, character variety, common password detection, entropy calculation.
*   **Password Generator:**
    *   Creates strong random passwords.
*   **Secure Storage:**
    *   Hashes passwords using bcrypt with automatic salting and a pepper.
*   **Two-Factor Authentication (2FA):**
    *   Implements TOTP with QR code provisioning for Google Authenticator/Authy.
*   **Brute Force Simulation:**
    *   Demonstrates why bcrypt is resistant to offline attacks.
*   **Complete Authentication System:**
    *   Registration and login with password + TOTP verification.

***

## **Project Structure**

    secure_password_project/
    │
    ├── main.py                # Entry point, menu-driven CLI
    ├── common_passwords.py    # Loads and checks common passwords
    ├── password_checker.py    # Analyzes password strength
    ├── password_generator.py  # Generates random passwords
    ├── entropy.py             # Calculates and interprets entropy
    ├── auth_utils.py          # Handles bcrypt hashing and pepper
    ├── totp_utils.py          # Implements TOTP and QR code generation
    ├── user_system.py         # Registration and login logic
    ├── brute_force_demo.py    # Simulates dictionary attacks
    └── users.json             # Stores user credentials (hashed) and TOTP secrets

***

## **How to Run**

### **1. Install Dependencies**

```bash
python -m pip install bcrypt pyotp qrcode pillow
```

### **2. Set Pepper (Optional but Recommended)**

```bash
export PEPPER="your-secret-pepper"
```

*(On Windows PowerShell use: `setx PEPPER "your-secret-pepper"`)*
If skipped, default pepper `"mysecretpepper"` is used.

### **3. Prepare Common Passwords File**

Create `common_passwords.txt` in the project folder with common passwords like:

    password
    123456
    qwerty
    admin

### **4. Run the Application**

```bash
python main.py
```

***



