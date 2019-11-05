def _init_(self,k):
    """初始化分类器"""
    assert k >=1,   "k must be valid"
    self.k = k
    self._x_train = None
    self._y_train = None

def fit(self,x_):