import socket
from _thread import *

print("Starting server...")

server = "127.0.0.1"
port = 5555

pos = [(100, 400), (850, 400)]
life = [100, 100]

def read_pos(str):
    str = str.split(",")
    return [int(str[0]), int(str[1])]

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server, port))
s.listen(2)

print("Waiting for connection...")

def client_thread(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ''

    while True:
        try: 
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            elif data == 'life':
                reply = life
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]
                
                print(f'Received from player {player}: {data}.')
                print(f'Sending to player {player}: {reply}')

            conn.sendall(str.encode(make_pos(reply)))
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




