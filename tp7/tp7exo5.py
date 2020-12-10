import matplotlib.pyplot as plt
from numpy.random import rand
import numpy as np

list_pas = []

def bern(a, b, p):
    r = rand()
    if r < p:
        return b
    else:
        return a

def marche(nb_pas):
    list_pas = [bern(-1, 1, 0.5) for i in range(nb_pas)]
    return np.cumsum(list_pas)

# Question 1
print(marche(10))
print(marche(100))
print(marche(5000))

# Question 2
for i in range(500):
    li = marche(500)
    # plt.plot(li)

# Question 3: les valeurs semble se recentrer autour de 0 ce qui est logique car
# il y a la même probabilité de faire un pas à gauche qu'un pas à droite
li2 = marche(100)
plt.hist(li, bins=range(-100, 100, 2), normed=1)

# Question 4: les valeurs sont cohérentes par rapport à la courbe
x = np.linspace(-100, 100, 2000)
plt.plot(x, (1 / (10 * np.sqrt(2 * np.pi) ) ) * np.exp( (-x**2) / (200) ) )

plt.show()
