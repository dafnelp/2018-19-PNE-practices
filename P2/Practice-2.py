import socket


class Seq:

    def __init__(self, strbases):

        self.bases = strbases

    def complement(self):

        base_complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        c_seq = []

        for character in self.bases:
            c_seq.append(base_complement[character])

        return ''.join(c_seq)

    def reverse(self):
        r_seq = []
        len_seq = len(self.bases)

        for i in self.bases:
            len_seq = len_seq - 1
            r_seq.append(self.bases[len_seq])

        return ''. join(r_seq)


# Connect to the server using a while loop for asking for different sequences

s_msg = True

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("Socket created")

    PORT = 8082
    IP = "212.128.253.64"

    s.connect((IP, PORT))

    str_msg = input("Please, enter a sequence of amino acids: ")
    str_msg = Seq(str_msg)

    seq_comp = str_msg.complement()
    seq_comp = Seq(seq_comp)
    seq_rev = seq_comp.reverse()

    s.send(str.encode(seq_rev))

    msg = s.recv(2048).decode("utf-8")
    print("MESSAGE FROM THE SERVER:")
    print(msg)

    s.close()

    print("The end")
