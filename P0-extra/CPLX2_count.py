with open('CPLX2.txt', 'r') as f:

    DNA_seq = f.read()

    while '>' in DNA_seq:
        replace_line = DNA_seq.find('\n')
        DNA_seq = DNA_seq[replace_line+1:]

    count_a = DNA_seq.count('A')
    count_c = DNA_seq.count('C')
    count_t = DNA_seq.count('T')
    count_g = DNA_seq.count('G')

    print('A:', count_a)
    print('C:', count_c)
    print('T:', count_t)
    print('G:', count_g)
