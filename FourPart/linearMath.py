import numpy as np
import matplotlib.pyplot as plt

'''实现最小二乘法的代码实现'''


# 定义 x轴,y轴
x = np.array([1.,2.,3.,4.,5.])
y = np.array([1.,3.,2.,3.,5.])

# # scatter"散开"  在图上建立 x,y坐标点
# plt.scatter(x,y)
# # 在图上建立 x,y坐标轴
# plt.axis([0,6,0,6])
# plt.show()

# 首先要计算x和y的均值
x_mean = np.mean(x)
y_mean = np.mean(y)

# a 的分子 num , 分母 d
num = 0.0
d = 0.0
for x_i,y_i in zip(x,y): # zip函数打包成[(x_i,y_i)...]的形式
    num = num + (x_i-x_mean)*(y_i-y_mean)
    d = d+(x_i-x_mean)**2
    print(x_i,y_i)
# a,b 代表 a,b的导数（a，b偏导） 看有道云最小二乘法a,b偏导
a = num/d
b = y_mean-a*x_mean
print(a,b)

# 在求出a,b之后 ，可以计算y的预测值，首先绘制模型直线：
y_hat = a*x+b
print(y_hat)

plt.scatter(x,y)  # 绘制散点图
plt.plot(x,y_hat,color='r') # 绘制直线
plt.axis([0,6,0,6])
plt.show()

# 然后进行预测
x_predict = 6
y_predict = a*x_predict + b
print(y_predict)









































