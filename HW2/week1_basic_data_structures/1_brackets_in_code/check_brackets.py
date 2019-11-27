# # python3

# from collections import namedtuple

# Bracket = namedtuple("Bracket", ["char", "position"])


# def are_matching(left, right):
#     return (left + right) in ["()", "[]", "{}"]


# def find_mismatch(text):
#     opening_brackets_stack = []
#     for i, next in enumerate(text):
#         if next in "([{":
#             # Process opening bracket, write your code here
#             pass

#         if next in ")]}":
#             # Process closing bracket, write your code here
#             pass


# def main():
#     text = input()
#     mismatch = find_mismatch(text)
#     # Printing answer, write your code here

# if __name__ == "__main__":
#     main()

# Initially I have not take a look at the above ready code:

def balance_pranthesis(my_list):
    from collections import deque
    my_stack=deque()
    for i in range(len(my_list)-1):
        my_stack.append(my_list[i])
        if my_list[i+1]!=')':
            my_stack.append(my_list[i+1])
        elif my_stack[i]==')':
            my_stack.pop(my_list[i+1])

        if my_list[i+1]!=']':
            my_stack.append(my_list[i+1])
        elif my_stack[i]==']':
            my_stack.pop(my_list[i+1])

        if my_list[i+1]!='}':
            my_stack.append(my_list[i+1])
        elif my_stack[i]=='}':
            my_stack.pop(my_list[i+1])
    if len(my_stack)==0:
        status='Successful'
    elif len(my_stack)!=0:
        status='Not - Successful'
    return status

# def balance_check(my_list):
#     from collections import deque
#     my_stack=deque()
#     for i, element in enumerate(my_list):
#         if element is a closing bracket:
#             if closing bracket is consistent with top of stack:
#                 pop from stack
#             else:
#                 raise error
#         else: #if opening bracket is seen:
#             push it to the stack
        

def balance_check(my_list):
    from collections import deque
    my_stack=deque()
    for i,element in enumerate(my_list):
        if element in [')',']','}']:
            if element==my_stack[0]:
                my_stack.pop()
            else:
                print(i)
                return i
        else:
            my_stack.append(element)
    print("success")
    return -1

# print(balance_pranthesis('[([()][]]'))
balance_check('[([()][]]')

