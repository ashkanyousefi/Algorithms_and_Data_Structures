# # python3

# import sys
# import threading


# def compute_height(n, parents):
#     # Replace this code with a faster implementation
#     max_height = 0
#     for vertex in range(n):
#         height = 0
#         current = vertex
#         while current != -1:
#             height += 1
#             current = parents[current]
#         max_height = max(max_height, height)
#     return max_height

# def main():
#     n = int(input())
#     parents = list(map(int, input().split()))
#     print(compute_height(n, parents))

# # In Python, the default limit on recursion depth is rather low,
# # so raise it here for this problem. Note that to take advantage
# # of bigger stack, we have to launch the computation in a new thread.
# sys.setrecursionlimit(10**7)  # max depth of recursion
# threading.stack_size(2**27)   # new thread will get stack of such size
# threading.Thread(target=main).start()

number_size=5
child_arrangement=['-1','0','4','0','3']
parent_assignment=[]

def tree_creation(number_size,child_arrangment):  
    for i in range(number_size):
        if child_arrangement[i]=='-1':
            parent_assignment[i]=[]
        else:
            parent_assignment[i]=child_arrangement[i]
    return parrent_assignment

print(tree_creation(number_size,child_arrangment))