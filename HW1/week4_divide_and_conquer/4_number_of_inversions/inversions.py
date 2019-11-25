# Uses python3
import sys

#%%

my_array=[1, 3, 1, 5, 6]

#%%

def element_rearrange(my_array):
    counter=0
    for i in range(len(my_array)-1):
        if my_array[i]>my_array[i+1]:
            counter+=1
            my_array[i],my_array[i+1]=my_array[i+1],my_array[i]
    return counter,my_array

#%%
print(element_rearrange(my_array))

#%%

# def get_number_of_inversions(a, b, left, right):
#     number_of_inversions = 0
#     if right - left <= 1:
#         return number_of_inversions
#     ave = (left + right) // 2
#     number_of_inversions += get_number_of_inversions(a, b, left, ave)
#     number_of_inversions += get_number_of_inversions(a, b, ave, right)
#     #write your code here
#     return number_of_inversions

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n, *a = list(map(int, input.split()))
#     b = n * [0]
#     print(get_number_of_inversions(a, b, 0, len(a)))
