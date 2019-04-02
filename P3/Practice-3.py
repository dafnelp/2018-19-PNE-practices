import socket

from Seq import Seq

PORT = 8080
IP = "127.0.0.1"
MAX_OPEN_REQUEST = 5


def valid_seq(seq_msg):
    """Function to know if the characters introduced by the
    client are a sequence of DNA.
    Parameters: seq_msg that corresponds to the message introduced
    by the client"""

    for letter in seq_msg:
        # Way that allow to recognize upper and lower introduced characters
        letter = letter.upper()
        if letter != 'A' and letter != 'C' and letter != 'G' and letter != 'T':
            # Open the error HTML file
            return False
    return True


def process_client(cs):
    # Reading the message from the client
    msg = cs.recv(2048).decode("utf-8")
    # Divide the message by parts
    msgs = msg.split("\n")
    # Where we store the sequences introduced by the client
    seq = msgs[0]
    seq = seq.upper()
    # Convert the string into an object
    seq_dna = Seq(seq)
    # Where we store the message to send to the client
    answer = ''

    # The client wants to know if the server is working
    if msg == "\n":
        cs.send(str.encode("ALIVE"))

    # Not requesting if the server is working
    else:
        # The sequence introduced by the client is correct
        if valid_seq(seq):
            answer = "OK\n"
            # Rest of the message of the client
            for i in range(1, len(msgs) - 1):
                operation = ""

                # Operations to perform
                if "len" in msgs[i]:
                    operation = seq_dna.len()

                if "complement" in msgs[i]:
                    operation = seq_dna.complement()

                if "reverse" in msgs[i]:
                    operation = seq_dna.reverse()

                if "countA" in msgs[i]:
                    operation = seq_dna.count_bases("A")

                if "countT" in msgs[i]:
                    operation = seq_dna.count_bases("T")

                if "countC" in msgs[i]:
                    operation = seq_dna.count_bases("C")

                if "countG" in msgs[i]:
                    operation = seq_dna.count_bases("G")

                if "percA" in msgs[i]:
                    operation = seq_dna.perc("A")

                if "percT" in msgs[i]:
                    operation = seq_dna.perc("T")

                if "percC" in msgs[i]:
                    operation = seq_dna.perc("A")

                if "percG" in msgs[i]:
                    operation = seq_dna.perc("A")

                answer = answer + str(operation) + "\n"
                print(answer)

        else:
            answer = "ERROR"

    cs.send(str.encode(answer))

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
