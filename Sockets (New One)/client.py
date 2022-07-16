import socket
import threading

nickname = input("Enter a nickname : ")

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',1234))





def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message=="NICK":
                client.send(nickname.encode('ascii'))
                print(nickname.encode('ascii'))
            else:
                print(message)

        except:
            print("An error occured")
            client.close()
            break
    
def send():
    while True:
        message = f'{nickname} : {input("Enter your message here : ")}'
        client.send(message.encode('ascii'))


r1 = threading.Thread(target=receive)
r1.start()

s1 = threading.Thread(target=send)
s1.start()
