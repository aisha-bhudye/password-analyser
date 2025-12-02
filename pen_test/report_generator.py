def generate_report(open_ports, found_files, vulnerabilities):
    print("PENETRATION TEST REPORT")

    print("Summary of Findings:\n")
    print(f"1. PORT SCAN - {len(open_ports)} open ports")
    print(f"2. FILE ENUM - {len(found_files)} files found")
    print(f"3. VULNERABILITIES - {len(vulnerabilities)} detected")

    print("\nOVERALL RISK LEVEL:")
    if len(vulnerabilities) >= 3:
        print("  HIGH")
    elif len(vulnerabilities) >= 1:
        print("  MEDIUM")
    else:
        print("  LOW")
