import socket
import termcolor

IP = "10.0.2.15"
PORT = 8082
MAX_OPEN_REQUESTS = 5


def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")

    # Print the received message, for debugging
    print()
    print("Request message: ")
    termcolor.cprint(msg, 'green')

    def process_info(f):
        """ Process the info introduced by the client request.
        Parameters:  f: file that should be open depending the request"""

        # Open the HTML file
        with open(f, "r") as r:
            content = r.read()

        status_line = "HTTP/1.1 200 ok\r\n"

        header = "Content-Type: text/html\r\n"
        header += "Content-Length: {}\r\n".format(len(str.encode(content)))

        response_msg = status_line + header + "\r\n" + content
        # Send the message to the client
        cs.send(str.encode(response_msg))

        # Close the socket
        cs.close()
    # Possible request of the client
    if "/ HTTP/1.1" in msg:
        process_info("index.html")
    elif "/blue HTTP/1.1" in msg:
        process_info("blue.html")
    elif "/pink HTTP/1.1" in msg:
        process_info("pink.html")
    else:
        process_info("error.html")

# MAIN PROGRAM

# create an INET, STREAMing socket


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(clientsocket)
