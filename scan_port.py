import socket
from concurrent.futures import ThreadPoolExecutor

target = str(input("Enter the target : ")).strip()
host = socket.gethostbyname(target)
port_range = str(input("Enter port range ex: 1-1024 : ")).strip()
begin, end = port_range.split("-")
begin = int(begin)
end = int(end)
thread = int(input("Enter the thread : "))
port_numbers = range(begin,end + 1)

def port_scanner(port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    if sock.connect_ex((host,port)) == 0:
        print(f"[+] {port}")
        sock.settimeout(0.5)
        try:
            banner = sock.recv(1024).decode(errors="Ignore").strip()
            if banner:
                print(f" {banner}\n")
        except sock.timeout:
            pass

worker = ThreadPoolExecutor(max_workers=thread)
worker.map(port_scanner,port_numbers)

