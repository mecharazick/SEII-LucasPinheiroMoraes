import socket

TCP_IP = '127.0.0.1'
FILE_PORT = 5005
DATA_PORT = 5006
FADDR = (TCP_IP, FILE_PORT)
DADDR = (TCP_IP, DATA_PORT)
FORMAT = 'utf-8'
timeout = 3
buf = 1024

sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_f.bind(FADDR)
sock_f.listen(1)

sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_d.bind(DADDR)
sock_d.listen(1)

while True:
    conn, addr = sock_f.accept()
    data = conn.recv(buf)
    if data:
        print(f'File name: {data}')
        file_name = data.strip()

    f = open(b'received/' + file_name, 'wb')

    conn, addr = sock_d.accept()
    while True:
        data = conn.recv(buf)
        if not data:
            break
        f.write(data)

    print(f'{file_name} Finish!')
    f.close()