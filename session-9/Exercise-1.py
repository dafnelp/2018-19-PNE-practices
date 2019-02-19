import socket

from termcolor import colored

PORT = 8080
IP = "212.128.253.95"
MAX_OPEN_REQUEST = 5


def process_client(cs):
    # Max length of the message and decode the message from bytes to strings
    # Reading the message from the client
    msg = cs.recv(2048).decode("utf-8")
    if msg == "exit":

        print("Message from the client: {}".format(msg))
        cs.send(str.encode('Program terminate'))


        cs.close()

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
