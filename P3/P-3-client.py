import socket
import termcolor

# SERVER IP, PORT
IP = "127.0.0.1"
PORT = 8080

while True:

    # Before connecting to the server, ask the user for a sequence of DNA
    msg_send = ""  # Where we store the message to send to the client
    msg = input("Introduce a DNA sequence and the operations you want to perform: ")  # Where the client should enter the message
    while len(msg) > 0:
        msg_send = msg_send + msg + "\n"
        msg = str(input(""))

    # If the user does not send any message
    if len(msg_send) == 0:
        send = "\n"

    # Creating the socket and connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send the message to the server
    s.send(str.encode(msg_send))

    # Receive the response
    response = s.recv(2048).decode()

    # Print the server's response
    termcolor.cprint("Response: {}".format(response), 'blue')

    s.close()
