import socket

c1 = socket.socket()
c1.connect(('localhost',9999))      ##replace the IP address(localhost) with the server's IP address if the server is running on a different machine in the same network
name = input("Enter your name: \n")
c1.send(bytes(name, 'utf-8'))

while True:
    msg = input(f"{name}: ")
    c1.send(bytes(msg, 'utf-8'))
    msg = c1.recv(1024).decode()
    print(msg)
    if msg.lower() == "bye":
        print("closing connection")
        c1.close()
        break