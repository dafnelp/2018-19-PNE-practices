from Seq import Seq

# Main program

s1 = Seq('ATTCCCAGGGTATATCCAGA')
s2 = Seq('CATGAT')
s3 = Seq(s1.complement())
s4 = Seq(s3.reverse())

bases1 = s1.bases
length_seq1 = s1.len()
count_bases1 = s1.count()
perc_bases1 = s1.perc()

print('Sequence 1:', bases1)
print('Length:', length_seq1)
print('Bases count:', count_bases1)
print('Bases percentage:', perc_bases1)

bases2 = s2.bases
length_seq2 = s2.len()
count_bases2 = s2.count()
perc_bases2 = s2.perc()

print('Sequence 2:', bases2)
print('Length:', length_seq2)
print('Bases count:', count_bases2)
print('Bases percentage:', perc_bases2)

bases3 = s3.bases
length_seq3 = s3.len()
count_bases3 = s3.count()
perc_bases3 = s3.perc()

print('Sequence 3:', bases3)
print('Length:', length_seq3)
print('Bases count:', count_bases3)
print('Bases percentage:', perc_bases3)

bases4 = s4.bases
length_seq4 = s4.len()
count_bases4 = s4.count()
perc_bases4 = s4.perc()

print('Sequence 4:', bases4)
print('Length:', length_seq4)
print('Bases count:', count_bases4)
print('Bases percentage:', perc_bases4)
