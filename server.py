import socket
from _thread import *

print("Starting server...")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(((socket.gethostname(), 1234)))
s.listen(2)

print("Waiting for connection...")

def clientthread(conn):
    reply = ""

    while True:
        msg = clientsocket.recv(1024)
        print(f"Message from {address}: {msg.decode('utf-8')}")

        reply = input("Reply: ")
        clientsocket.send(bytes(reply, "utf-8"))

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    start_new_thread(clientthread, (clientsocket, address))




