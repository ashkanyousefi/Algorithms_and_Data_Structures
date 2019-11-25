# %%
item_number, capacity = tuple(map(int, input('').split()))
item_weight_value=[tuple(map(int,input('').split())) for _ in range(item_number)]  

# %%

def max_value(item_list):
    global capacity
    items=[(w, v, v/w) for v, w in item_list]
    print(items)
    items=sorted(items, key=lambda it: it[2], reverse=True)
    print(items)
    total_value=0
    for each in items:
        if capacity > 0:
            pick_value=min(each[0], capacity)
            capacity=capacity-pick_value
            total_value += each[2]*pick_value
    return total_value

#%%
print(max_value(item_weight_value))
