from sklearn.model_selection import  train_test_split

from irisDemo import iris

""" 使用skl 中的 train_test_split """

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=666)
