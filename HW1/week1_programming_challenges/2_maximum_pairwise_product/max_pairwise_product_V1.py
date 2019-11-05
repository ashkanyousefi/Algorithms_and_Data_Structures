# python3

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    if n>=2:
        max_product=numbers[0]*numbers[1]
    else:
        max_product=0
    return max_product


if __name__ == '__main__':
    input_numbers = [int(x) for x in input().split()]
    input_numbers.sort(reverse=True)
    print(max_pairwise_product(input_numbers))