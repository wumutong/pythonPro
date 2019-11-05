from collections import Counter
from math import sqrt
import numpy as np

class OnePartDemoPlus:
    def __init__(self,k):
        """初始化分类器"""
        assert k >=1,"k must be valid"
        self.k = k
        self._x_train = None
        self._y_train = None

    def fit(self,x_train,y_train):
        """根据训练数据集x_train 和 y_train训练KNN分类器"""
        assert x_train.shape[0] == y_train.shape[0],"the size of X_train must be equal to the size of y_train"
        assert self.k <= x_train.shape[0],"the size of X_train must be at least k"
        self._x_train = x_train
        self._y_train = y_train
        return self

    def predict(self,x_predict):
        """给定预测数据集x_predict,返回表示x_predict结果的向量"""
        assert self._x_train is not None and self._y_train is not None,"must fit before predict!"
        assert x_predict.shape[1] == self._x_train.shape[1],"the feature number of X_predict must be equal to X_train"
        y_predict = [self._predict(x) for x in x_predict]
        return np.array(y_predict)

    def _predict(self,x):
        distances = [sqrt(np.sum((x_train - x)**2)) for x_train in self._x_train]
        nearest = np.argsort(distances)
        top_k_y = [self._y_train[i] for i in nearest]
        votes = Counter(top_k_y)
        return votes.most_common(1)[0][0]

    def __repr__(self):
        return "Knn(k=%d)" % self.k

kx=6
knn_clf = OnePartDemoPlus(kx) # k=6
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
knn_clf.fit(X_train, y_train)
# narray的总元素个数为N 矩阵的第一维度大小为1，第二维度大小为N。
X_predict = X_train.reshape(1,-1)
y_predict = knn_clf.predict(X_predict)
print(y_predict)























