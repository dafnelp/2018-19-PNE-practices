import socket

# Create a socket for communicating with the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket created")

PORT = 8083
IP = "10.0.2.15"

# Connect to the server

s.connect((IP, PORT))

# Message of the client

client_msg = input("Enter a sequence of amino-acids: ")

# Send the message to the server

s.send(str.encode(client_msg))

msg = s.recv(2048).decode("utf-8")

print("MESSAGE FROM THE SERVER:")
print(msg)

s.close()

print("The end")
