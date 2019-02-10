class Seq:
    def __init__(self, strbases):

        self.bases = strbases

    def len(self):

        return len(self.bases)

    def count(self):

        count_a = "A: {}".format(self.bases.count('A'))
        count_c = "C: {}".format(self.bases.count('C'))
        count_t = "T: {}".format(self.bases.count('T'))
        count_g = "G: {}".format(self.bases.count('G'))

        return count_a, count_c, count_t, count_g

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

    def perc(self):

        perc_a = "A: {} %".format(round(100.0 * self.bases.count('A') / len(self.bases), 1))
        perc_c = "C: {} %".format(round(100.0 * self.bases.count('C') / len(self.bases), 1))
        perc_t = "T: {} %".format(round(100.0 * self.bases.count('T') / len(self.bases), 1))
        perc_g = "G: {} %".format(round(100.0 * self.bases.count('G') / len(self.bases), 1))

        return perc_a, perc_c, perc_t, perc_g
