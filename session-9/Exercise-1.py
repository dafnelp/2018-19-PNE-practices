import socket
import sys
from termcolor import colored

PORT = 8082
IP = "10.0.2.15"
MAX_OPEN_REQUEST = 5


def process_client(cs):
    # Reading the message from the client
    msg = cs.recv(2048).decode("utf-8")
    msg = msg.lower()

    if msg == "exit":
        cs.send(str.encode("Program terminate"))

        cs.close()
        sys.exit(0)

    else:
        msg = colored(msg, 'blue')
        print("Message from the client: {}".format(msg))

        # sending the message back to the client --- echo server
        cs.send(str.encode(msg))

        cs.close()


# Create a socket for connecting to the clients

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}".format(serversocket))

while True:

    print("Waiting for connections at: {}, {}".format(IP, PORT))

    (clientsocket, address) = serversocket.accept()

    # Process the client request
    print("Attending client: {}".format(address))

    process_client(clientsocket)
