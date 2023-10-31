import socket
import sys

TCP_IP = '127.0.0.1'
FILE_PORT = 5005
DATA_PORT = 5006
FADDR = (TCP_IP, FILE_PORT)
DADDR = (TCP_IP, DATA_PORT)
FORMAT = 'utf-8'
buf = 1024
file_name = sys.argv[1]

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(FADDR)
    sock.send(file_name.encode(FORMAT))
    sock.close()

    print(f'Sending {file_name} ...')
    
    f = open(file_name, "rb")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(DADDR)
    data = f.read()
    sock.send(data)

finally:
    sock.close()
    f.close()