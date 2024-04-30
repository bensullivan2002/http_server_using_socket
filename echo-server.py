# echo-server.py

import socket

HOST = 'localhost'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    conn, addr = s.accept()  # conn represents the client socket, and addr represents the client address
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

# Need to add a response message from the server

# Need to add functionality to go back to listening once the data is received from the client, rather than just
# closing the connection and stopping
