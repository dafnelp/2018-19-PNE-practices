import socket

# Configure the Server's IP and PORT

PORT = 8082
IP = "10.0.2.15"
MAX_OPEN_REQUESTS = 5

# Counting the number of connections

number_con = 0

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serversocket.bind((IP, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        # Another connection!
        number_con += 1

        # Print the conection number
        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        # Create the class
        class Seq:

            def __init__(self, strbases):

                self.bases = strbases

            # Function for the complement of the sequence
            def complement(self):

                base_complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
                c_seq = []

                for character in self.bases:
                    c_seq.append(base_complement[character])

                return ''.join(c_seq)

        # Read the message from the client, if any
        msg = clientsocket.recv(2048).decode("utf-8")
        # Converting the string sending by the client in the class to use the function .complement()
        msg = Seq(msg)
        msg_seq = msg.complement()
        print("Complementary of the sequence introduced by the client: {}".format(msg_seq))

        # Send the message
        send_bytes = str.encode(msg_seq)
        # We must write bytes, not a string
        clientsocket.send(send_bytes)
        clientsocket.close()

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()
