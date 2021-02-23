import socket
import threading
import sys

IP = "127.0.0.1"
PORT = 20557

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((IP, PORT))

def sendMessage():
    while True:
        user_message = input("Message >> ")
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