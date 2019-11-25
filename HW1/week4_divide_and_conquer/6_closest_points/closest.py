# Uses python3
# %%
import sys
import math
import itertools

# %%
my_points = [(2, 3), (4, 5), (6, 5)]

# %%

def distance_calculations(x1, y1, x2, y2):
    return math.sqrt((x1-y1) ^ 2+(x2-y2) ^ 2)

# %%

def select_approximate_points(my_points):
    point_selection = itertools.permutations(my_points)
    for item in point_selection:
        di = distance_calculations(item[0][0],item[0][1],item[1][0],item[1][1])
        di_min = 10**6
        if di < di_min:
            di_min = di
            cartesian_points = (a, b)
    return di_min, cartesian_points

#%%
select_approximate_points(my_points)

# %%

def minimum_distance(x, y):
    # write your code here
    return 10 ** 18

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))


