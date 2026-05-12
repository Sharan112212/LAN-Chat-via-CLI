# LAN Chat via CLI

A multi-client LAN chat application built using Python sockets and threading.

This project allows multiple clients connected to the same network to communicate with each other through a central server using a command-line interface.

---

## Features

- Multi-client chat system
- Real-time message broadcasting
- Threaded client handling
- Timestamped messages
- LAN-based communication using TCP sockets
- Separate send and receive threads on client side

---

## Technologies Used

- Python
- Socket Programming
- Multithreading (`threading` module)
- TCP/IP Networking

---

## Project Structure

```bash
LANChat/
│
├── server.py
├── client.py
├── .gitignore
└── README.md
```

---

## How It Works

### Server
- Creates a TCP socket
- Accepts incoming client connections
- Stores connected clients
- Creates a dedicated thread for each client
- Broadcasts received messages to other connected clients

### Client
- Connects to the server
- Uses one thread for sending messages
- Uses another thread for receiving messages
- Supports real-time communication

---

## Running the Project

### Start the Server

```bash
py server.py
```

### Start the Client

```bash
py client.py
```

> Replace `localhost` with the server machine's IP address when using different systems on the same LAN.

---

## Example

```text
[23:45] Manoj: Hello
[23:46] Sharan: Hi!
```

---

## Current Limitations

- Basic CLI interface
- No encryption
- No persistent chat history
- Terminal input/output may overlap during simultaneous messaging
- Limited error handling

---

## Future Improvements

- GUI version using Tkinter or PyQt
- Private messaging
- User authentication
- Better terminal UI
- Async I/O implementation
- File sharing support

---

## Learning Outcomes

This project helped in understanding:

- TCP socket communication
- Client-server architecture
- Concurrent programming using threads
- Shared state management
- Real-time networking concepts
- Blocking I/O behavior

---

## Author

Sharan