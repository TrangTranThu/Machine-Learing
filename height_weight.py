# 2 cach : 1 su dung bang cong thuc, 1 cach bang thu vien
import numpy as np # khai bao numpy
import matplotlib.pyplot as plt #khai bao thu vien ve  do thi

# height(cm)  de ma tran chuyen vi de tinh theo cong thuc
x = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T

#weight(kg)
y = np.array([[ 49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T

plt.xlabel

#visualize data

plt.scatter(x, y) # bieu dien cac toa do la dau cham
plt.xlabel('Height (cm)') # ten tren truc x
plt.ylabel('Weight (kg)') # ten tren truc y
plt.show()