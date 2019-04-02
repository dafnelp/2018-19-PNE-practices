import socket

from Seq import Seq

# Connect to the server using a while loop for asking for different sequences
PORT = 8080
IP = "127.0.0.1"

while True:
    str_msg = input("Please, enter a sequence of amino acids: ")
    str_msg = Seq(str_msg)
    # Performing the operations of the complement of the sequence and then the reverse
    seq_comp = str_msg.complement()
    seq_comp = Seq(seq_comp)
    seq_rev = seq_comp.reverse()

    # Crating the socket and connecting to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send the message to the server
    s.send(str.encode(seq_rev))

    # Receive the response
    msg = s.recv(2048).decode("utf-8")

    # Print the response
    print("MESSAGE FROM THE SERVER:")
    print(msg)

    s.close()
