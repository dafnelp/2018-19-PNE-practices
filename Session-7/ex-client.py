import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket created")

PORT = 8081
IP = "212.128.253.77"

# Connect to the server

s.connect((IP,PORT))

s.send(str.encode("HELLO ITS ME"))

msg = s.recv(2048).decode("utf-8")
print("MESSAGE FROM THE SERVER:")
print(msg)

s.close()

print("The end")