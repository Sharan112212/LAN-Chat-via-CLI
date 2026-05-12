import socket
import threading


def receive(c):
    while True:
        msg = c.recv(1024).decode()
        print(msg)
        if msg.lower() == "":
            print("closing connection")
            c.close()
            break

def send(c,name):
    while True:
        msg = input(f"{name}: ")
        c.send(bytes(msg, 'utf-8'))
        if msg.lower() == "":
            print("closing connection")
            c.close()
            break

def client_program():

    c = socket.socket()
    c.connect(('localhost',9999))      ##replace the IP address(localhost) with the server's IP address if the server is running on a different machine in the same network
    name = input("Enter your name: \n")
    c.send(bytes(name, 'utf-8'))

    receive_thread = threading.Thread(target = receive, args=(c,))
    receive_thread.start()
    send_thread = threading.Thread(target = send, args=(c,name))
    send_thread.start()

client_program()