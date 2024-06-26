# echo-client.py

import socket

HOST = 'localhost'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, World!')
    data = s.recv(1024)

print(f"Received {data!r}")  # Could we also use {data.decode('utf-8') here?
