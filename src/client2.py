import socket

c2 = socket.socket()
c2.connect(('localhost',9999))        ##replace the IP address(localhost) with the server's IP address if the server is running on a different machine in the same network
name = input("Enter your name: \n")
c2.send(bytes(name, 'utf-8'))

while True:
    msg = c2.recv(1024).decode()
    print(msg)
    if msg.lower() == "bye":
        print("closing connection")
        c2.close()
        break
    msg = input("enter your message:\n")
    c2.send(bytes(msg, 'utf-8'))