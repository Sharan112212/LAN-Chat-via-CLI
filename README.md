# Python Socket Chat Application

A simple terminal-based chat application built using Python sockets.

This project demonstrates basic client-server communication using TCP sockets where two clients can exchange messages through a central server.

---

## Features

* Two-client communication
* Server-side message forwarding
* Username support
* LAN-based communication
* Terminal chat interface
* Basic connection closing using `bye`

---

## Technologies Used

* Python
* Socket Programming
* TCP/IP Networking

---

## Project Structure

```text
server.py
client1.py
client2.py
```

---

## How It Works

1. The server waits for two client connections.
2. Client 1 sends a message.
3. The server forwards the message to Client 2.
4. Client 2 replies.
5. The server forwards the reply back to Client 1.
6. The process continues until a user sends:

```text
bye
```

---

## How to Run

### Start the Server

```bash
py server.py
```

### Start Client 1

```bash
py client1.py
```

### Start Client 2

```bash
py client2.py
```

---

## Important Notes

* All systems should be connected to the same network/hotspot for LAN communication.
* Replace the server IP in the client files with your local IPv4 address if using multiple devices.

---

## Concepts Learned

* Socket creation
* TCP communication
* bind(), listen(), accept()
* send() and recv()
* Client-server architecture
* Basic networking protocols

---

## Future Improvements

* Multi-client support
* GUI interface
* Threading for simultaneous messaging
* Message encryption
* Internet/global network support
