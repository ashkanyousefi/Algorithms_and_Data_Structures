import numpy as np

#Main functions
def allocation_function(capacity,item):
    return capacity%item

weight=np.array([100,70,60,40,25],dtype=np.float)
values=np.array([10,7,30,20,5],dtype=np.float)
# value_per_unit=[x/y for x,y in zip(values/weight)]
value_per_unit=values/weight
value_per_unit=np.sort(value_per_unit,axis=None)

while (capacity>0):
    for item in value_per_unit:
        updated_capacity=allocation_function(capacity,item)
    capacity=updated_capacity







