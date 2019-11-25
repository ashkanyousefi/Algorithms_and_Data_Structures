# Uses python3
#%%
import sys
import itertools

#%%

my_array=[3,4,5,6,7,8,9,11,13]


#%%

def partion_creation(my_array):
    sum_target=sum(my_array)//3
    new_array=itertools.permutations(my_array)
    final_list=[]

    for item in new_array:
        if sum(item)==sum_target:
            final_list.append(item)

    return final_list
























#%%
aa=itertools.product(range(3), repeat=2)
for i in aa:
    print(aa)

#%%

def partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)
        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

#%%


aa=itertools.permutations(range(3),2)
print(aa)

# %%
