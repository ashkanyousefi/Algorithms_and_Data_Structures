n=7

def primative_calculator(n):

    factor_three=n//3
    remainder_three=n%3
    factor_two=remainder_three//2
    remainder_two=remainder_three%2
    print('the minimum number of factors are equal to {} plus {} and {} number of factor one'\
    .format(factor_three,factor_two,remainder_two))
    print('The total number of factors are {}'.format(factor_three+factor_two+remainder_two))

primative_calculator(n)

# import sys

# def optimal_sequence(n):
#     sequence = []
#     while n >= 1:
#         sequence.append(n)
#         if n % 3 == 0:
#             n = n // 3
#         elif n % 2 == 0:
#             n = n // 2
#         else:
#             n = n - 1
#     return reversed(sequence)

# input = sys.stdin.read()
# n = int(input)
# sequence = list(optimal_sequence(n))
# print(len(sequence) - 1)
# for x in sequence:
#     print(x, end=' ')



# The solution is similar to the money exchange approach by dividing the number into 
# Different numbers and find the target value by all possible combinations 
# Then select the minimum number of operations from the available combinations.
