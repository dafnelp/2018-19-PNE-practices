with open('DNA_seq.txt', 'r') as f:

    for line in f:

        line = line.replace('\n', '')

        length = len(line)

        count_a = line.count('A')
        count_c = line.count('C')
        count_t = line.count('T')
        count_g = line.count('G')

        print(line)
        print('Total number of bases for each line:', length)
        print('A:', count_a)
        print('C:', count_c)
        print('T:', count_t)
        print('G:', count_g)
