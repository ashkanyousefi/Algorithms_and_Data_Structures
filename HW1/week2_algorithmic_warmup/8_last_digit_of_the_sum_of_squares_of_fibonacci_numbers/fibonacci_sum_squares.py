# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def last_digit(n):
    if n <= 1:
        return 1
    return (last_digit(n-1) + last_digit(n-2)) % 10, 

def squared_sum_fib_last_digit(n):
    return (last_digit(n) * last_digit(n+1)) % 10


if __name__ == '__main__':
    n = input()
    n = int(n)
    print(squared_sum_fib_last_digit(n))


# The above method is slow and the square method as shown need to be implemented.


