my_array=[2,3,5,5,6,6,6]

def majority_finder(my_array):
    # my_array.append(10**20)
    print(my_array)
    register=[]
    my_array.sort()
    result='There is no majority in the provided array'
    
    item_value=my_array[0]
    item_count=0
    item_position=0

    for item in range(len(my_array)):
        if  item_value != my_array[item] or item == (len(my_array) - 1):
            item_count=item-item_position
            if item == (len(my_array) - 1):
                item_count += 1
            register.append((item_value,item_count))
            item_value=my_array[item]
            item_position=item
        print(item,register)
        

    for item in register:
        if item[1]>=len(my_array)//2:
            result='There is a mojority in the array with the value: {}'.format(item[0])
    return result

if __name__=='__main__':
    print(majority_finder(my_array))


