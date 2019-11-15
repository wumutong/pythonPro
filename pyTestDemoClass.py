# 两个下划线开头的函数是声明该属性为私有，不能在类的外部被使用或访问
class initDemo:
    def __init__(self, name, score):
        self.name = name
        self.score = score
# Knn(k=张三) 会按照我们需要输出对象的形式原样输出，
# 否则会输出内存地址，面向程序员
    def __repr__(self):
        return "Knn(k=%s)" % self.name
#[Value: 张三]  如果两个都有会显示这个 __str__ 面向用户的
    def __str__(self):
        return '[Value: %s]' % self.name
    def MyPrint(self):
        return self.name
    # 相当于构造函数 __init__(必须这样写) 第一个参数必须 ->  self
classa =  initDemo("张三",1)
print(classa.MyPrint()) # 张三
print(classa)











