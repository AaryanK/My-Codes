import socket
import threading 

HEADER = 64
PORT = 4040
SERVER = '127.0.0.1'
ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

def respond(connection):
    response = input('enter something here')
    connection.send(response.encode(FORMAT))

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDRESS)

def handle_client(connection,address,c):
    print(f'[NEW CONNECTION] {address} connected')
    connected = True
    while connected:
        msg_length = connection.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = connection.recv(msg_length).decode(FORMAT)
            print(msg)
            th = threading.Thread(target=respond,args=(connection))
            if msg == DISCONNECT_MESSAGE:
                connected = False


def start():
    server.listen()
    print(f'SERVER starting on : {socket.gethostname()}')
    print(f'SERVER started on ip :{SERVER} and on server {socket.gethostname()}')
    c = []
    while True:
        connection, address = server.accept()
        c.append(connection)
        thread = threading.Thread(target=handle_client, args=(connection, address,c))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1} {connection} joined")

start()