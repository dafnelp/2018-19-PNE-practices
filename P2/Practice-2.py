import socket

from Seq import Seq

# Connect to the server using a while loop for asking for different sequences
PORT = 8082
IP = "10.0.2.15"

s_msg = True

while True:
    str_msg = input("Please, enter a sequence of amino acids: ")
    str_msg = Seq(str_msg)

    seq_comp = str_msg.complement()
    seq_comp = Seq(seq_comp)
    seq_rev = seq_comp.reverse()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((IP, PORT))

    s.send(str.encode(seq_rev))

    msg = s.recv(2048).decode("utf-8")
    print("MESSAGE FROM THE SERVER:")
    print(msg)

    s.close()

    print("The end")
