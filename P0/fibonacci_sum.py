print('Program to calculate the sum of the fibonacci series')


def fibonacci_sum(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        # list where we are going to store the values
        fibonacci = [0] * (n+1)
        fibonacci[1] = 1
        # We establish that we start counting from 1
        sum_fib = fibonacci[1]

        for i in range(2, n+1):
            # We fill the positions in the list
            fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
            sum_fib = sum_fib + fibonacci[i]

        return sum_fib


# Main program
num = int(input('Introduce an n:'))
final = fibonacci_sum(num)
print('The sun of the fibonacci numbers is:', final)
