import socket
import select

UDP_IP = '127.0.0.1'
IN_PORT = 5005
FORMAT = 'utf-8'
timeout = 3
buf = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, IN_PORT))

while True:
    data, addr = sock.recvfrom(buf)
    if data:
        print(f'File name: {data}')
        file_name = data.strip()

    f = open(b'received/' + file_name, 'wb')

    while True:
        ready = select.select([sock], [], [], timeout)
        if ready[0]:
            data, addr = sock.recvfrom(1024)
            f.write(data)
        else:
            print(f'{file_name} Finish!')
            f.close()
            break