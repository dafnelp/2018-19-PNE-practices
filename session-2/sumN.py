print('Function to sum n numbers')


def sumn(n):

    total = 0
    for i in range(n):
        total += i + 1

    return total


# Main program
num = int(input('Please introduce n: '))
total_sum = sumn(num)

print('The total sum is', total_sum)
