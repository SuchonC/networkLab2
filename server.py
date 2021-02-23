import threading
import socket

IP = '127.0.0.1'
PORT = 20557

connections = []

def clientThreadFunc(conn, addr):
    conn.send(b"Welcome to the room!")
    while True:
        try:
            message = conn.recv(2048)
            if message:
                msg = f"<{addr[0]}> : {message.decode()}"
                print(msg)
                broadcast(msg.encode(), conn)
        except:
            exit()

def broadcast(msg, msg_owner):
    for client_conn in connections:
        if client_conn != msg_owner:
            try:
                client_conn.send(msg)
            except:
                client_conn.close()
                remove(client_conn)

def remove(conn):
    if conn in connections:
        connections.remove(conn)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((IP, PORT))
server.listen()
print(f"Listening at {IP}:{PORT}")

while True:
    conn, addr = server.accept()
    connections.append(conn)
    print(f"{addr} connected")

    client_thread = threading.Thread(target=clientThreadFunc, args=((conn, addr)))
    client_thread.start()