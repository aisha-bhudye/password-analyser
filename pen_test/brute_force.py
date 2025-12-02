import time

def simulate_brute_force():
    print("SECTION 5: BRUTE FORCE SIMULATION")
    print("Simulating dictionary attack with common passwords...\n")

    common_passwords = ['password', '123456', 'admin', 'letmein', 'qwerty']

    for i, password in enumerate(common_passwords, 1):
        time.sleep(0.1)
        print(f"  Attempt {i}: Testing '{password}'...")

    print("\nSimulation complete")
