
import numpy as np
from FourPart.linearMathPro import SimpleLinearRegression
import matplotlib.pyplot as plt
"""调用自己封装好的 最小二乘法"""

x = np.array([1.,2.,3.,4.,5.])
y = np.array([1.,3.,2.,3.,5,])
x_predict = np.array([6])
reg = SimpleLinearRegression()
reg.fit(x,y)


reg.predict(x_predict)
print(reg.a_)
print(reg.b_)

y_hat = reg.predict(x)

plt.scatter(x,y)
plt.plot(x,y_hat,color='r')
plt.axis([0,6,0,6])
plt.show()