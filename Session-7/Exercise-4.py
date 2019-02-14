import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket created")

PORT = 8082
IP = "10.0.2.15"

# Connect to the server

s.connect((IP, PORT))

s.send(str.encode("Hello, I'm testing the client-server in my computer"))

msg = s.recv(2048).decode("utf-8")
print("MESSAGE FROM THE SERVER:")
print(msg)

s.close()

print("The end")
