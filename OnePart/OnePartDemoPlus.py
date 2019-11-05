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

























