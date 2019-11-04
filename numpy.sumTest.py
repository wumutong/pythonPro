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

#结果的含义是：距离最小的点在distances数组中的索引是1，
#第二小的点索引是3... 近到远是哪些点
distances = [5,1,3,2,4]
nearest = ny.argsort(distances)
print(nearest)
