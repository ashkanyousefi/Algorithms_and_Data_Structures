# python3
def max_pairwise_product(numbers):
    max_product = 0
    if len(numbers)==2:
        max_product=numbers[0]*numbers[1]
    else:
        max1, max2 = -1, -1
        for item in numbers:
            if item > max1:
                max2 = max1
                max1 = item
            elif item > max2:
                max2 = item
        max_product = max1 * max2
    return max_product


if __name__ == '__main__':
    arr_len = input()
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))

