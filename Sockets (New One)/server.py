import socket
import threading

HOST = '127.0.0.1'
PORT = 1234

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()


clients = []
nicks = []


def broadcast(message):
    for c in clients:
        c.send(message.encode("ascii"))

def handle(client):
    while True:
        try:
            message = client.recv(1024).decode("ascii")
            broadcast(message=message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicks[index]
            broadcast(f"{nickname} has left us :(")
            nicks.remove(nickname)
            break


def receive():
    while True:
        client,address = server.accept()
        print(f"Connected with {str(address)}")

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicks.append(nickname)
        clients.append(client)

        print(f"{str(address)} is now {nickname}")
        broadcast(f"{nickname} has now joined the party\n")
        client.send('connected to the server'.encode('ascii'))

        t = threading.Thread(target=handle,args=(client,))
        t.start()

print("server started")
receive()