import socket

# definição dos parâmetros do cliente como cabeçalho da mensagem
# porta da conexão
# endereço do servidor
# tupla de conexão
# mensagem padrão para encerrar conexão
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT)

#cria socket para conexão
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# função que gerencia envio de mensagens
# primeiro envia uma mensagem com o tamanho do texto, identada
# para possuir a quantidade de bytes do cabeçalho
# depois envia a mensagem
# e printa uma mensagem de resposta recebida do servidor
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - send_length)
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Hello World!")
input()
send("Hello Everyone!")
input()
send("Hello Tim!")
send(DISCONNECT_MESSAGE)