import matplotlib.pyplot as plt
from numpy.random import randint

A = []
for i in range(300):
    A.append([randint(0, i+1) for j in range(300)])

plt.matshow(A, cmap='hot')
plt.show()
