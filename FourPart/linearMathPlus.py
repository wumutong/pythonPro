# 我们注意到，在计算参数a时：  num = num + (x_i-x_mean)*(y_i-y_mean)
# 向量w和向量v，每个向量的对应项，相乘再相加。其实这就是两个向量“点乘”
# 这样我们就可以使用numpy中的dot运算，非常快速地进行向量化运算。
# 注意：向量化是非常常用的加速计算方式，特别适合深度学习等需要训练大数据的领域。

#两种方式 对于 y=wx+b,若w,x都是向量，那么，可以用两种方式来计算，第一个是for循环
# 第一种
# y = 0
# for i in range(n):
#     y += w[i]*x[i]
#     y += b

#第二种
# y = np.dot(w,x) +b
# 两者的速度相差几百倍


import numpy as np
import time

a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time()
c = np.dot(a, b)
toc = time.time()
print("c: %f" % c)
print("vectorized version:" + str(1000*(toc-tic)) + "ms")

c = 0
tic = time.time()
for i in range(1000000):
    c += a[i] * b[i]
toc = time.time()
print("c: %f" % c)
print("for loop:" + str(1000*(toc-tic)) + "ms")