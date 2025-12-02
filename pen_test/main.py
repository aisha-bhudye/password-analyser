from port_scanner import scan_ports
from file_enum import enumerate_files
from database_analysis import analyze_database
from vulnerability import assess_vulnerabilities
from brute_force import simulate_brute_force
from report_generator import generate_report


def main():
    print("SIMPLE PENETRATION TEST - Refactored Version")

    if input("Continue? (yes/no): ").strip().lower() != 'yes':
        print("Test cancelled.")
        return

    host = "127.0.0.1"
    ports = [22, 80, 443, 5000, 5432, 8080]

    open_ports = scan_ports(host, ports)
    found_files = enumerate_files()
    analyze_database()
    vulnerabilities = assess_vulnerabilities()
    simulate_brute_force()
    generate_report(open_ports, found_files, vulnerabilities)


if __name__ == "__main__":
    main()
