import socket

from Seq import Seq

PORT = 8082
IP = "10.0.2.15"
MAX_OPEN_REQUEST = 5


def process_client(cs):
    # Reading the message from the client
    msg = cs.recv(2048).decode("utf-8")
    first_msg = msg.find("n")
    # Where we store the sequences introduced by the client
    seq = msg[0:first_msg - 1]
    seq = seq.upper()
    # Where the commands introduced by the client are stored
    command = msg[first_msg + 1:]
    command = command.lower()
    # Convert the string into an object
    seq_dna = Seq(seq)

    if msg == " ":
        cs.send(str.encode("ALIVE"))
    else:
        invalid_char = False
        for letter in seq:
            letter = letter.upper()
            if letter != 'A' and letter != 'C' and letter != 'G' and letter != 'T':
                invalid_char = True

        if invalid_char:
            cs.send(str.encode("ERROR"))
            cs.close()
        else:
            cs.send(str.encode('OK'))

            if "len" in command:
                len_seq = seq_dna.len()
                print(len_seq)
            if "complement" in command:
                comp_seq = seq_dna.complement()
                print(comp_seq)
            if "reverse" in command:
                rev_seq = seq_dna.reverse()
                print(rev_seq)
            if "counta" in command or "countt" in command or "countc" in command or "countg" in command:
                count_bases = seq_dna.count()
                print(count_bases)
            if "perca" in command or "perct" in command or "pecc"in command or "percg" in command:
                perc_bases = seq_dna.perc()
                print(perc_bases)

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
