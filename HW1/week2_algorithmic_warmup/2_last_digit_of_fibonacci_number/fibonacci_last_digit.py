# Uses python3
# import sys

# def get_fibonacci_last_digit_naive(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current

#     return current % 10

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n = int(input)
#     print(get_fibonacci_last_digit_naive(n))


# Can I use the following instead

def get_last_digit(n):
    if n<=2:
        return 1
    temp = get_last_digit(n-1) + get_last_digit(n-2)

    return temp%10

n=input('Enter the number in a Fibonacci sequence: ')


