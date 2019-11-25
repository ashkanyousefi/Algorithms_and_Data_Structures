# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd
#%%
def gcd_fast(a, b):
    mod_value=2
    while(mod_value>1):
        mod_value=a%b
        if mod_value==0:
            gcd_answer=b
        else:
            a=b
            b=mod_value
    return gcd_answer

if __name__ == "__main__":
    ab = input()
    a, b = map(int, ab.split())
    print((a,b))
    print(gcd_fast(a, b))
    print(gcd_naive(a, b))

# Please take a look












    