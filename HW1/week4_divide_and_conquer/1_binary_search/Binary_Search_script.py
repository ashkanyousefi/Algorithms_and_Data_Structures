
main_array = [1, 2, 13, 4, 5, 6]
# main_array = input('Enter the series of the number with space to be considered as a search array: ').split()
# main_array=[int(x) for x in main_array]
# search_number=map(int,input('Enter the number to search in the array: ').split())
search_number = [23]
main_array.sort()
print(main_array)


def element_finder(main_array, search_number):
    selected_array = main_array
    while(len(selected_array) >= 1):
        pointer_index = len(selected_array)//2
        if search_number > selected_array[pointer_index]:
            selected_array = selected_array[pointer_index:]
            pointer_index = len(selected_array)//2
        if search_number < selected_array[pointer_index]:
            selected_array = selected_array[:pointer_index]
            pointer_index = len(selected_array)//2
        if search_number == selected_array[pointer_index]:
            status = 'Item found'
        else:
            status = 'Item not found'
        return search_number, status

def recursive_binary_search(main_array, search_number):
    print(main_array)
    if len(main_array) == 0:
        return -1
    if len(main_array) == 1:
        if main_array[0] == search_number:
            return 0
        else:
            return -1

    mid_id = len(main_array)//2
    mid_element = main_array[mid_id]
    if search_number == mid_element:
        return mid_id
    elif search_number > mid_element:
        result = recursive_binary_search(main_array[mid_id+1:], search_number)
        if result == -1:
            return -1
        else:
            return result + mid_id
    else:
        return recursive_binary_search(main_array[:mid_id], search_number)
        

# I have tried to make it recursive by updating the return to
# return element_finder(main_array,specific_number)
# However it goes for the index out of range


if __name__ == '__main__':
    for sn in search_number:
        # print(element_finder(main_array, sn))
        print("{}: {}".format(sn, recursive_binary_search(main_array, sn)))

