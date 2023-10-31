import socket
import threading

# definição de parâmetros de conexão,
# como tamanho do cabeçalho da mensagem principal (payload)
# endereço do servidor, definido como o endereço ip da máquina
# na conexão atual
# tupla de endereço (ip, porta)
# padrão de texto do payload
# mensagem padrão de desconexão
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

# criação do objeto servidor e definição da forma de conexão
# a forma de conexão é baseada no socket de rede com ipv4
# e o segundo parâmetro é o tipo de socket utilizado
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

#função que gerencia conexão, recebendo dados da mensagem
def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected.')

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            
            print(f'[{addr}] {msg}')
            conn.send("Msg received".encode(FORMAT))
    
    conn.close()

# função de inicialização do servidor, cria uma thread
# para cuidar de cada conexão
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.activeCount() - 1}')

#inicializaçao do servidor
print("[STARTING] server is starting...")
start()