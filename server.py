import socket
from _thread import *

print("Starting server...")

server = "127.0.0.1"
port = 5555

status = [(100, 400, 100, 0), (850, 400, 100, 0)]

def read_status(str):
    str = str.split(",")
    return [int(str[0]), int(str[1]), int(str[2]), int(str[3])]

def make_status(tup):
    return str(tup[0]) + "," + str(tup[1]) + "," + str(tup[2]) + "," + str(tup[3])


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server, port))
s.listen(2)

print("Waiting for connection...")


def client_thread(conn, player):
    conn.send(str.encode(make_status(status[player])))
    reply = ''

    while True:
        try:
            data = read_status(conn.recv(2048).decode())
            status[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = status[0]
                else:
                    reply = status[1]

                print(f'Received from player {player}: {data}.')
                print(f'Sending to player {player}: {reply}')

            conn.sendall(str.encode(make_status(reply)))
        except Exception as e:
            print(e)

    conn.close()


current_player = 0

while True:
    client_socket, address = s.accept()
    print(f"Connection from {address} has been established!")

    start_new_thread(client_thread, (client_socket, current_player))
    current_player += 1

print("Server is shutting down...")
client_socket.close()
