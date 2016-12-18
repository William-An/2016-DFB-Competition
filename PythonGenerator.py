import random
import numpy as np
def mapgenerator(zero_map):
    zero_map=zero_map
    for i in range(len(zero_map)):
        for j in range(len(zero_map[i])):
            zero_map[i,j]=random.randint(0,7)
    size=random.randint(3,5)
    i=random.randint(2,15)
    j=random.randint(2,15)
    print(size)
    print(i)
    print(j)
    for a in range(size+1):
        for b in range(size+1):
            zero_map[i+a,j+b]=1
    return zero_map
zero=np.zeros((20,20))
map=mapgenerator(zero)
print(map)
