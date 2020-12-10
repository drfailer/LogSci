from numpy.random import rand
import matplotlib.pyplot as plt
import numpy as np

# Retourne un pas aléatoire :
def un_pas():
    r = rand()
    if r < 0.25:
        return [1, 0]
    elif r < 0.5:
        return [0, 1]
    elif r < 0.75:
        return [-1, 0]
    else:
        return [0, -1]

# Modélisation d'une marche 2D
def marche_2D(n):
    pos = [0, 0]
    li_pas = [(pos + un_pas()) for i in range(n)]
    li = np.cumsum(li_pas)
    plt.plot(li)
    plt.show()

marche_2D(1000)
