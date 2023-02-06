import socket
from _thread import *

print("Starting server...")

server = "127.0.0.1"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server, port))
s.listen(2)

print("Waiting for connection...")

def clientthread(conn):
    reply = ""

    while True:
        msg = clientsocket.recv(1024)
        print(f"Message from {address}: {msg.decode('utf-8')}")

        reply = msg.decode("utf-8")
        clientsocket.send(bytes(reply, "utf-8"))

        if not msg:
            print(f"Connection from {address} has been terminated!")
            break

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    clientsocket.send(bytes("Welcome to the server!", "utf-8"))

    start_new_thread(clientthread, (clientsocket,))

print("Server is shutting down...")
clientsocket.close()




