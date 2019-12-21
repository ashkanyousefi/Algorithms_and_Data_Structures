# python3
 
import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
 
class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
 
        def compute_height(self):
                # Replace this code with a faster implementation
                maxHeight = 0
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        while i != -1:
                                height += 1
                                i = self.parent[i]
                        maxHeight = max(maxHeight, height)
                return maxHeight
 
def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())
 
threading.Thread(target=main).start()

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