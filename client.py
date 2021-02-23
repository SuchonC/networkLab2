import socket
import threading
import sys

if len(sys.argv) != 3 :
    print(f"Usage : {sys.argv[0]} <IP> <Port>")
    exit()

IP = sys.argv[1]
PORT = int(sys.argv[2])

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((IP, PORT))

def sendMessage():
    while True:
        user_message = input()
        server.send(user_message.encode())

def recvMessage():
    while True:
        message = server.recv(2048)
        if message:
            print(message.decode())

send_message_thread = threading.Thread(target=sendMessage)
send_message_thread.start()

recv_message_thread = threading.Thread(target=recvMessage)
recv_message_thread.start()