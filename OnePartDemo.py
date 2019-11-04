import numpy as np
import matplotlib.pyplot as plt
# raw_data_x是特征，raw_data_y是标签，0为良性，1为恶性
raw_data_X = [[3.393533211, 2.331273381],
              [3.110073483, 1.781539638],
              [1.343853454, 3.368312451],
              [3.582294121, 4.679917921],
              [2.280362211, 2.866990212],
              [7.423436752, 4.685324231],
              [5.745231231, 3.532131321],
              [9.172112222, 2.511113104],
              [7.927841231, 3.421455345],
              [7.939831414, 0.791631213]
             ]
raw_data_y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
# 设置训练组
X_train = np.array(raw_data_X)
y_train = np.array(raw_data_y)
# 将数据可视化
plt.scatter(X_train[y_train==0,0],X_train[y_train==0,1], color='g', label = 'Tumor Size')
plt.scatter(X_train[y_train==1,0],X_train[y_train==1,1], color='r', label = 'Time')
plt.xlabel('Tumor Size')
plt.ylabel('Time')
plt.axis([0,10,0,5])
plt.show()

from math import sqrt
# 测试x是恶性肿瘤还是良性肿瘤
x=[8.90933607318, 3.365731514]
#x=np.array(x1)
distances = []
# 用来记录x到样本数据集中每个点的距离
for x_train in X_train:
    d = sqrt(np.sum((x_train - x) ** 2))
    distances.append(d)
    # 使用列表生成器，一行就能搞定，对于X_train中的每一个元素x_train都进行前面的运算，把结果生成一个列表
distances = [sqrt(np.sum((x_train - x) ** 2)) for x_train in X_train]

print(distances)

# 根据 numpy.argsort对数组进行从小到大
# 距离最小的点在distances数组中的索引是7，
# 第二小的点索引是8... 近到远是哪些点
nearest = np.argsort(distances)
print(nearest)

k = 6
topK_y = [y_train[i] for i in nearest[:k]]
print(topK_y)




























