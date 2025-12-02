def print_section(title):
    print(f"{title}")


import socket


def scan_ports(host, ports):
    print_section("SECTION 1: PORT SCANNING")
    print(f"Scanning {host} for open ports...")
    print(f"Testing ports: {ports}\n")

    open_ports = []

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))

        if result == 0:
            open_ports.append(port)
            print(f"Port {port}: OPEN ")
        else:
            print(f"Port {port}: CLOSED ")

        sock.close()

    print(f"\nScan complete: {len(open_ports)} open port(s) found")
    return open_ports
