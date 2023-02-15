import socket
from _thread import *

print("Starting server...")

server = "127.0.0.1"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server, port))
s.listen(2)

print("Waiting for connection...")

def clientthread(conn, player):
    conn.send(str.encode("500,150"))
    reply = ''

    while True:
        msg = clientsocket.recv(1024).decide("utf-8")
        print(f"Message from {address}: {msg}")
        
        reply = msg.decode("utf-8")
        
        print(f"Sending message to {address}: {reply}")
        clientsocket.send(bytes(reply, "utf-8"))

        if not msg:
            print(f"Connection from {address} has been terminated!")
            break


currentPlayer = 0
while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    start_new_thread(clientthread, (clientsocket, currentPlayer))
    currentPlayer += 1

print("Server is shutting down...")
clientsocket.close()




