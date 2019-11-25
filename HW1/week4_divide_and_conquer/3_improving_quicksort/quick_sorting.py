

# This is a Naive implementation and I still not sure how to determine the number of required loops


my_array=[2,3,9,3,4,2,2]
import random

def quicksort(my_array):
    print(my_array)
    if len(my_array)<=1:
        result=my_array
    else:
        pivot_id=random.randint(a=0,b=len(my_array)-1)
        pivot_value = my_array[pivot_id]
        new_list_small=[]
        new_list_large=[]
        
        for item_id, item in enumerate(my_array):
            if item<=pivot_value and item_id!=pivot_id: 
                new_list_small.append(item)      
            if item>pivot_value:
                new_list_large.append(item)
        print(pivot_value, new_list_small, new_list_large)
        input()
        result_small=quicksort(new_list_small)
        result_large=quicksort(new_list_large)
        result=result_small+[pivot_value]+result_large
    return result

    
if __name__ == "__main__":
    print(quicksort(my_array))

#The rearrangement of the array can be done in place without the need for using two different arrays.
#The above approach is called implacement.



# l=0

# def element_rearrange(my_array):
#     for index_item in range(len(my_array)-1):
#         if my_array[index_item]>my_array[index_item+1]:
#             my_array[index_item],my_array[index_item+1]=my_array[index_item+1],my_array[index_item]
#     return my_array

# r=len(my_array)-1
# for i in range(l,r):
#     selected_array=element_rearrange(my_array[0:i])
#     print(selected_array)



# if __name__ == "__main__":
#     print(element_rearrange(my_array))

#The following example is recommended by the course as a code skeleton

# import sys
# import random

# a=[2,3,2,8,5,3]
# def partition3(a, l, r):
#     #write your code here
#     pass

# def partition2(a, l, r): 
#     x = a[l]
#     j = l
#     for i in range(l + 1, r + 1):
#         if a[i] <= x:
#             j += 1
#             a[i], a[j] = a[j], a[i]
#     a[l], a[j] = a[j], a[l]
#     return j

# def randomized_quick_sort(a, l, r):
#     if l >= r:
#         return
#     k = random.randint(l, r)
#     a[l], a[k] = a[k], a[l]
#     #use partition3
#     m = partition2(a, l, r)
#     randomized_quick_sort(a, l, m - 1);
#     randomized_quick_sort(a, m + 1, r);

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n, *a = list(map(int, input.split()))
#     randomized_quick_sort(a, 0, n - 1)
#     for x in a:
#         print(x, end=' ')




