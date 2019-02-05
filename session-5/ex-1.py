def count_a(seq):
    """Counting the number of As in the sequence"""

    # Counter nfor the As
    result = 0

    for b in seq:
        if b == 'A':
            result += 1

    # Return the result
    return result


# Main program
s = "AGTATATAGAGAGA"
na = count_a(s)
print('The number of As is:', na)