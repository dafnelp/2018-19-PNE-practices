import socket

# SERVER IP, PORT
IP = "212.128.253.95"
PORT = 8080

while True:

    # The client is blocking the server....  NOT A GOOD DESIGN!!!
    msg = input("> ")
    # The client is not connected yet, the server is not blocked

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send the request message to the server
    s.send(str.encode(msg))

    # Receive the servers response
    response = s.recv(2048).decode()

    # Print the server's response
    print("Response: {}".format(response))

    s.close()
