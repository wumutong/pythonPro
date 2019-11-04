import numpy as ny
a= [[1,2],[4,6]]
b=[0,1]
array1 = ny.array(a)
array2 = ny.array(b)
# sum = (x1-x2) + (y1-y2)
# **2 就是平方 **3 就是三次方
for x in array1:
    print(ny.sum(x-b))
    print(ny.sum(x-b)**2)
