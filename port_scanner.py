import socket

target = input("Enter Target IP or Hostname: ")

print(f"\nScanning {target}...")
print("-" * 30)

common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS"
}

open_ports = []

for port, service in common_ports.items():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} ({service}) is OPEN")
        open_ports.append(port)

    sock.close()

print("\n" + "-" * 30)
print("Scan Complete!")

if open_ports:
    print("Open Ports Found:", open_ports)
else:
    print("No open ports found.")