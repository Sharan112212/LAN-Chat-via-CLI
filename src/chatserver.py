import socket
import threading
from datetime import datetime

def localtime():
    now = datetime.now()
    return now.strftime("%H:%M")

def accept_connections(s):
    clients = []
    while True:
        c, addr = s.accept()
        sender = c.recv(1024).decode()
        print("connected with", addr, sender)
        client_r = threading.Thread(target = receive_from_client, args=(c, sender,clients))
        clients.append(c)
        client_r.start()

def receive_from_client(c, sender,clients):
    while True:
        msg = c.recv(1024).decode()
        print(f"[{localtime()}] {sender}: {msg}")
        if msg.lower() == "bye" :
            print("closing connection")
            c.close()
            break
        for client in clients:
            if client!=c:
                client.send(bytes(f"[{localtime()}] {sender}: {msg}", 'utf-8'))

def main():
    s = socket.socket()
    s.bind(('localhost',9999))
    s.listen(2)
    print("waiting for connections")
    accept_connections(s)
main()