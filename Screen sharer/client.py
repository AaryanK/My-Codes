from multiprocessing.connection import Client
from vidstream import ScreenShareClient
import threading

client = ScreenShareClient('192.168.1.65',9999)

t1 = threading.Thread(target=client.start_stream)
t1.start()

while input("")!="STOP":
    continue

client.stop_stream()
