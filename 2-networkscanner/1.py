from scapy.all import *


def network_scan(target_ip, start_port, end_port):
    open_ports = []

    for port in range(start_port, end_port + 1):
        # Create a TCP SYN packet
        packet = IP(dst=target_ip) / TCP(dport=port, flags="S")

        # Send the packet and capture the response
        response = sr1(packet, timeout=1, verbose=0)

        # Check if a response was received
        if response is not None:
            # Check if the response has the SYN-ACK flag set
            if response[TCP].flags == "SA":
                open_ports.append(port)

    return open_ports


# Example usage
target_ip = "192.168.187.134"
start_port = 1
end_port = 100

open_ports = network_scan(target_ip, start_port, end_port)

print("Open ports:")
for port in open_ports:
    print(port)