import socket
from _thread import *
import pickle
from game import Game

server = "localhost"
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)

print("Waiting for Connection, Server Started")

connected = set()
games = { }
IDCount = 0


def Threaded_Client(conn, p, gameID):
    global IDCount
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()

            if gameID in games:
                game = games[gameID]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.player(p, data)

                    reply = game
                    conn.sendall(pickle.dumps(reply))
            else:
                break
        except:
            break

    print("Lost Connection")
    try:
        del games[gameID]
        print("Closing Game", gameID)
    except:
        pass
    IDCount -=1
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connect to:", addr)

    IDCount += 1
    p = 0
    gameID = (IDCount - 1) // 2
    if IDCount % 2 == 1:
        games[gameID] = Game(gameID)
        print("Creating a new game...")
    else:
        games[gameID].ready = True
        p = 1

    start_new_thread(Threaded_Client, (conn, p, gameID))
