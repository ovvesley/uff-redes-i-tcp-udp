import socket
import random
import time

HOST = '127.0.0.1'
PORT = 65432

id = random.randint(1, 100)

message = 'Oi, eu sou o cliente ' + str(id)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp:
    tcp.connect((HOST, PORT))

    while True:
        tcp.sendall(message.encode())
        data = tcp.recv(1024)
        print(data.decode('utf-8'))
        time.sleep(1)