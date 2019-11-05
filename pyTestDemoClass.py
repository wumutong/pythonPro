# 两个下划线开头的函数是声明该属性为私有，不能在类的外部被使用或访问
class initDemo:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        return "Knn(k=%d)" % self.k
    def MyPrint(self):
        return self.name
    # 相当于构造函数 __init__(必须这样写) 第一个参数必须 ->  self
print(initDemo("张三",1).MyPrint()) # 张三
