import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
# 手写数字数据集，封装好的对象，可以理解为一个字段
from irisDemo import iris

digits = datasets.load_digits()
# 可以使用keys()方法来看一下数据集的详情
print(digits.keys())#输出：dict_keys(['data', 'target', 'target_names', 'images', 'DESCR'])

# 对于sklearn.datasets中提供的数据描述
# 5620张图片，每张图片有64个像素点即特征（8*8整数像素图像），
# 每个特征的取值范围是1～16（sklearn中的不全），
# 对应的分类结果是10个数字print(digits.DESCR)

# 特征的shape
X = digits.data
print(X.shape) # (1797, 64)
# 标签的shape
y = digits.target
print(y.shape) # (1797,)
# 标签分类
print(digits.target_names)# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#  去除某一个具体的数据，查看其特征以及标签信息
some_digit = X[666]
print(some_digit)#array([ 0.,  0.,  5., 15., 14.,  3.,  0.,  0.,  0.,  0., 13., 15.,  9.,15.,  2.,  0.,  0.,  4., 16., 12.,  0., 10.,  6.,  0.,  0.,  8.,16.,  9.,  0.,  8., 10.,  0.,  0.,  7., 15.,  5.,  0., 12., 11.,0.,  0.,  7., 13.,  0.,  5., 16.,  6.,  0.,  0.,  0., 16., 12.,15., 13.,  1.,  0.,  0.,  0.,  6., 16., 12.,  2.,  0.,  0.])
# 也可以这条数据进行可视化
some_digmit_image = some_digit.reshape(8, 8)
plt.imshow(some_digmit_image, cmap = matplotlib.cm.binary)
plt.show()














































