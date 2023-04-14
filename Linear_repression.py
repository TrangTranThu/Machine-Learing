import numpy as np
import matplotlib.pyplot as plt

x = [20, 21, 18, 180, 160, 170]
y = [50, 40, 60, 85, 50, 75]

x = np.array([x]).T
y = np.array([y]).T
one = np.ones((x.shape[0], 1))
Xbar = np.concatenate((x, one), axis = 1)

X = np.linalg.pinv(Xbar.transpose().dot(Xbar)).dot(Xbar.transpose()).dot(y)
print(X)

y0 = x*X[0] +x[1]
print(y0)

plt.plot(x, y, 'ro')
plt.plot(x, y0)
plt.show()
