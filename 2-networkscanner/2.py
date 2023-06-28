from scapy.all import *
import optparse


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


def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--ip", dest="target_ip", help="Change the Interface")
    parser.add_option("-s", "--sport", dest="start_port", help="Change the start_port")
    parser.add_option("-e", "--eport", dest="end_port", help="Change the end_port")
    return parser.parse_args()


(options, arguments) = get_argument()

# Example usage
target_ip = options.target_ip
start_port = int(options.start_port)
end_port = int(options.end_port)

open_ports = network_scan(target_ip, start_port, end_port)

print("Open ports:")
for port in open_ports:
    print(port)