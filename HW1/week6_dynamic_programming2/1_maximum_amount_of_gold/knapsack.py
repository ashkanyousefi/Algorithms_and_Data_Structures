# Uses python3
#%%
import sys
import itertools

#%%

# I have assumed that the list of items are given in the w and the total capacity of the Knapsack is 
# equal to the W 

def optimal_weight(W, w):
    # write your code here

    all_combinations=itertools.permutations(w)
    total_permutations=[(sum(all_combinations),all_combinations) for item in all_combinations]

    max_value=0
    for i in range(len(total_permutations)):
        if total_permutations[i][0]>max_value:
            max_value=total_permutations[i][0]
            item_index=i

    optimum_combination=total_permutations[item_index][1:2]
    return optimum_combination

#%%
    for item in all_combinations:
        if sum(item)<=W:
            analyzed_elements.append(item)
        
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))

#One appraoch will be to generate a full llist of possibilities and then sort the summation to see the highest value which can be generated 
# The maximum capacity of the knapsack also considered.

