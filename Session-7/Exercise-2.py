# Programming the client

import socket


s_msg = True

while True:
    # Create a socket for communicating with the server using a while loop to ask for a multiple messages

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("Socket created")

    PORT = 8086
    IP = "212.128.253.76"

    # Connected to the server

    s.connect((IP, PORT))
    client_msg = input("Enter a mesagge:")

    s.send(str.encode(client_msg))

    msg = s.recv(2048).decode("utf-8")
    print("MESSAGE FROM THE SERVER:")
    print(msg)

    s.close()

    print("The end")
