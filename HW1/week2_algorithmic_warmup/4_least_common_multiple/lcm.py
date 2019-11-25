
print('test')

# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

from gcd import *

def lcm(a, b):
    gcd_result = gcd_fast(a,b)
    total=a*b
    final_result=total/gcd_result
    print(final_result)
    return final_result

if __name__ == '__main__':
    ab = input()
    a, b = map(int, ab.split())
    print(lcm(a, b))

