print('Program to calculate the nth term of the fibonacci series')


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        total_sum = fibonacci(n-1) + fibonacci(n-2)
        return total_sum


# Main program
num = int(input('Introduce an n: '))
final_num = fibonacci(num)

print('The number is', final_num)
