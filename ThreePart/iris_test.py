import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

# 加载花数据
iris = datasets.load_iris()
x = iris.data
y = iris.target
#准备 测试集 和 训练集
X_train,X_test,y_train,y_test = train_test_split(iris.data,iris.target,test_size=0.2,random_state=666)

# 使用数据归一化的方法
from sklearn.preprocessing import  StandardScaler  #-计算训练集的平均值和标准差，以便测试数据集使用相同的变换
standardScaler = StandardScaler()
# 归一化的过程跟训练模型一样
standardScaler.fit(X_train)
standardScaler.mean_
standardScaler.scale_ # 表述数据分布范围的变量，替代std_

# 使用 transform 通过居中和缩放执行标准化
X_train_standard = standardScaler.transform(X_train)
print(X_train_standard)
print("**************************我是分隔符*******************************")
X_test_standard = standardScaler.transform(X_test)
print(X_test_standard)































































