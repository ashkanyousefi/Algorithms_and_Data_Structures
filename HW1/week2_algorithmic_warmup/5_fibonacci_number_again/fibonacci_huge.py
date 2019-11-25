# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))

    #The above method is not effective for the large numbers and as a result the periodic method need to be implemented.


def get_fibonacci_huge_naive(n):
    if n<=1:
        return n

    return (get_fibonacci_huge_naive(n-1) + get_fibonacci_huge_naive(n-2))%10 

    
    





