from vidstream import StreamingServer
import threading

server = StreamingServer('192.168.1.65',9999)

t1 = threading.Thread(target=server.start_server)
t1.start()

while input("")!="STOP":
    continue

server.stop_server()



