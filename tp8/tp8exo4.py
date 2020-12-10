import numpy as np
import matplotlib.pyplot as plt
        
mat = np.array([[1, 1, 1],
                 [1, 0, 1],
                 [1, 1, 1]])

def sierpinski(mat):
    l1 = np.hstack((mat, mat))
    l1 = np.hstack((l1, mat))
    nul = np.zeros((mat.shape))
    l2 = np.hstack((mat, nul))
    l2 = np.hstack((l2, mat))
    grid = np.vstack((l1, l2))
    grid = np.vstack((grid, l1))

    return grid


for _ in range(5):
    mat = sierpinski(mat)

    
plt.matshow(mat)
plt.show()

