# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0
    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))

# I think the correct approach is to calculate the fibonacci value up to the start of from_ and save it in a specific value 
# then run another loop and calculate the fibonacci value for from to 

