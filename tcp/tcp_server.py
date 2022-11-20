import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp:
    tcp.bind((HOST, PORT))

    tcp.listen()
    print('Server ready!')
    conn, addr = tcp.accept()

    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data.decode('utf-8'))

            conn.sendall(b'Prazer, eu sou o servidor.')
