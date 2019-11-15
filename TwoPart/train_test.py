from sklearn import datasets
import numpy as np
iris = datasets.load_iris()

X = iris.data
y = iris.target
#查看导入数据的格式和形状
print(X.shape)
print(y.shape)

#因为要形成训练和测试，但是测试要随机取样,不能就直接简单的进行后20%的样本取样，所以需要对其shuffle
# 方法1
# 使用concatenate函数进行拼接，因为传入的矩阵必须具有相同的形状。
# 因此需要对label进行reshape操作，reshape(-1,1)表示行数自动计算，1列。axis=1表示纵向拼接。
tempConcat = np.concatenate((X, y.reshape(-1,1)), axis=1)
# 拼接好后，直接进行乱序操作
np.random.shuffle(tempConcat)
# 再将shuffle后的数组使用split方法拆分
shuffle_X,shuffle_y = np.split(tempConcat, [4], axis=1)
# 设置划分的比例
test_ratio = 0.2
test_size = int(len(X) * test_ratio)
#对测试数据集 和 训练数据集进行划分
X_train = shuffle_X[test_size:]
y_train = shuffle_y[test_size:]
X_test = shuffle_X[:test_size]
y_test = shuffle_y[:test_size]



#第二种方法
# 将x长度这么多的数，返回一个新的打乱顺序的数组
# 注意，数组中的元素不是原来的数据，而是混乱的索引
shuffle_index = np.random.permutation(len(X))
print(shuffle_index)
# 指定测试数据的比例
test_ratio = 0.2
test_size = int(len(X) * test_ratio)
test_index = shuffle_index[:test_size]
train_index = shuffle_index[test_size:]
#把打乱的index下标 传入X y矩阵中
X_train = X[train_index]
X_test = X[test_index]
y_train = y[train_index]
y_test = y[test_index]





















