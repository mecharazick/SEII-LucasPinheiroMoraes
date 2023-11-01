import socket
import select
import errno
import sys

HEADER_LENGTH = 10

HOST = '127.0.0.1'
PORT = 1234
ADDR = (IP, PORT)
ENCODING = 'utf-8'

my_username = input("Username: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADDR)
client_socket.setblocking(False)

username = my_username.encode(ENCODING)
username_header = f'{len(username):<HEADER_LENGTH}'.encode(ENCODING)
client_socket.send(username_header + username)

while True:
    message = input(f'{my_username} > ')
    if message:
        message = message.encode(ENCODING)
        message_header = f'{len(message):<HEADER_LENGTH}'.encode(ENCODING)
        client_socket.send(message_header + message)

    try:
        while True:
            username_header = client_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                print("connection closed by the server")
                sys.exit()
            username_length = int(username_header.decode(ENCODING).strip())
            username = client_socket.recv(username_length).decode(ENCODING)

            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode(ENCODING).strip())
            message = client_socket.recv(message_length).decode(ENCODING)

            print(f'{username} > {message}')

    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error', str(e))
            sys.exit()
        continue

    except as e:
        print('General error', str(e))
        sys.exit()