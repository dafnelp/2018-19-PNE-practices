def count_bases(seq):
    """Counting the number of A, C, T and G in the sequence"""

    # Counter for the bases

    count_a = seq.count('A')
    count_c = seq.count('C')
    count_t = seq.count('T')
    count_g = seq.count('G')

    dict_bases = dict(zip(['A', 'C', 'T', 'G'], [count_a, count_c, count_t, count_g]))

    value_a = dict_bases.get('A')
    value_c = dict_bases.get('C')
    value_t = dict_bases.get('T')
    value_g = dict_bases.get('G')

    tl = len(seq)

    if tl > 0:
        perc_a = {'A percentage': round(100.0 * value_a / tl, 1)}
        perc_c = {'C percentage': round(100.0 * value_c / tl, 1)}
        perc_t = {'T percentage': round(100.0 * value_t / tl, 1)}
        perc_g = {'G percentage': round(100.0 * value_g / tl, 1)}

    else:
        return 0
    length_seq = {'The length of the sequence is': tl}

    # Return the result

    return length_seq, dict_bases, perc_a, perc_c, perc_t, perc_g


# Main program

s = input("Please enter the sequence: ")
n_base = count_bases(s)
print(n_base)
