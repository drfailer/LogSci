from numpy.random import rand
import matplotlib.pyplot as plt


def bern(a, b, p):
    r = rand()
    if r < p:
        return b
    else:
        return a

# Création d'une liste de 100000 valeurs de {-1, 1} à l'aide de la fonction bern
li = [bern(-1, 1, 0.3) for i in range(100000)]
plt.hist(li, bins = [-1.5, -0.5, 0.5, 1.5])
plt.show()
