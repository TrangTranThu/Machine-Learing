import numpy as np
import matplotlib.pyplot as plt

x = [47, 50, 53, 58, 63, 65, 68, 70, 73, 75, 78, 80, 83]
y = [2499, 1299,  497, 1850, 4100, 11298, 5050, 20047, 26499, 54499, 36499, 42098, 45050]

x = np.array([x]).T
one = np.ones((x.shape[0], 1), dtype = int)
Xbar = np.concatenate((x, one), axis = 1)
Xbar
plt.plot(x, y, 'ro')

A = np.linalg.inv(Xbar.transpose().dot(Xbar)).dot(Xbar.transpose()).dot(y)
print(A)
# x0 = np.array([50, 100]).T
y0 = x * A[0] + A[1]
plt.plot(x, y, 'ro')
plt.plot(x, y0)
plt.show()