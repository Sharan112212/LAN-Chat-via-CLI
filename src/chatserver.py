import socket
from datetime import datetime

def localtime():
    now = datetime.now()
    return now.strftime("%H:%M:%S")



s = socket.socket()

s.bind(('localhost',9999))         ##replace the IP address(localhost) with 0.0.0.0 if you want to accept connections from any machine in the same network

s.listen(2)
print("waiting for connections")

c1, addr1 = s.accept()
sender1 = c1.recv(1024).decode()
print("connected with", addr1, sender1)
c2, addr2 = s.accept()
sender2 = c2.recv(1024).decode()
print("connected with", addr2, sender2)

while True:
    msg1 = c1.recv(1024).decode()
    print(f"[{localtime()}] {sender1}: {msg1}")
    c2.send(bytes(f"[{localtime()}] {sender1}: {msg1}",'utf-8'))
    msg2 = c2.recv(1024).decode()
    print(f"[{localtime()}] {sender2}: {msg2}")
    c1.send(bytes(f"[{localtime()}] {sender2}: {msg2}",'utf-8'))
    if msg1.lower() == "bye" or msg2.lower() == "bye":
        print("closing connection")
        c1.close()
        c2.close()
        break