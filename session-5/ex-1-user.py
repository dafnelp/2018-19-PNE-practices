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
s = input("Please enter the sequence: ")
na = count_a(s)
print('The number of As is:', na)

# Calculate the total sequence length
tl = len(s)

# Calculate the percentage of As in the sequence
if tl > 0:
    perc = round(100.0 * na / tl, 1)
else:
    perc = 0

print('The total length is:', tl)
print('The percentage of A is:', perc, '%')
