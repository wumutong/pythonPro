from sklearn import datasets

from  TwoPart.train_test_split import train_test_split
iris = datasets.load_iris()

X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)


from OnePart.OnePartDemoPlus import OnePartDemoPlus
#使用我们knn(上)所创建的工具类
my_kNNClassifier = OnePartDemoPlus(k=3)
#初始化相关训练集
my_kNNClassifier.fit(X_train,y_train)
#测试
y_predict = my_kNNClassifier.predict(X_test)

# 两个向量的比较，返回一个布尔型向量，对这个布尔向量（false=1，true=0）sum，
print(sum(y_predict == y_test)) #8
print(sum(y_predict == y_test)/len(y_test)) #0.26666666666666666




























