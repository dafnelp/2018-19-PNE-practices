import socket

# Create a socket for communicating with the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket created")

PORT = 8082
IP = "10.0.2.15"

# Connect to the server

s.connect((IP, PORT))

# Message of the client

client_msg = input("Enter a sequence of amino-acids: ")

# Send the message to the server

s.send(str.encode(client_msg))

# Receiving the message
msg = s.recv(2048).decode("utf-8")

# Printing the message
print("Complementary of the sequence introduced:")
print(msg)

s.close()

print("The end")
