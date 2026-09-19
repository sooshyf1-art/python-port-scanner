import socket
import time

open_ports = []
serv = "Unknown"

def scan_port(host, port):
    sock = socket.socket()
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    sock.close()
    if result == 0:
        try:
            serv = socket.getservbyport(port)
        except:
            serv = "Unknown"
        open_ports.append(port)
        return True, serv


host = input("IP Address: ")
start_port = int(input("Start Port: "))
end_port = int(input("End Port: "))
print(f"Scanning {host}...")

start_time = time.time()

count = 0

for port in range(start_port, end_port):
    result = scan_port(host, port)
    if result:
        serv = result[1]
        count = count + 1
        print(f"Port {port} {serv} - Open")
end_time = time.time()
elapsed = end_time - start_time
print(f"Scan finished in {elapsed} seconds,  {count} ports have opened, {open_ports} {serv} open. (prod by sooshyf)")