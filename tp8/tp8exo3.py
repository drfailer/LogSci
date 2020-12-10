import numpy as np

# Définition des matrices :
A = np.array([1, 2],
             [3, 4])

B = np.array([2, -1],
             [2, 7])

C = np.array([1, 1, 1, 1],
             [2, 2, 2, 2])

x = np.array([1],
             [-2])

y = np.array([5, 1, -0.5])

z = np.array([7, 7])

D = np.zeros((10, 20))

E = 7 * np.ones((7, 7))

I = np.eye(8)


# Question 1 :
print(A + B)
print(A @ B)
print(A * B)
print(A @ C)
print(A @ x)
print(10 * C)
print(z @ C)
print(x + z)

