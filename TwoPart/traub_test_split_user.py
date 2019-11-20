import numpy as np
from sklearn import datasets

from  TwoPart.train_test_split import train_test_split
iris = datasets.load_iris()

X = iris.data
y = iris.target


# 调用我们编写的随机取样测试方法
X_train, X_test, y_train, y_test = train_test_split(X, y)
# 输出我们我编写的随机取样测试方法
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

from OnePart.OnePartDemoPlus import OnePartDemoPlus
# 查看 生成的测试数据
knn_clf = OnePartDemoPlus(k=3)
knn_clf.fit(X_train, y_train)
y_predict = knn_clf.predict(X_test)
# 比对y_predict和y_test结果是否一致
print(sum(y_predict == y_test)/len(y_test))






























