from numpy.random import randint
import matplotlib.pyplot as plt


# Modélisation de 100 jeux
def pf():
    L = randint(0, 2, 100)
    return sum(L)

a = 0
b = 0
for i in range(2000):
    c = pf()
    if c > 53:
        a+=1
    elif c <= 40:
        b+=1  
      
print("La probabilité qu'il y ai plus de 53 piles est", a / 20, "%.")
print("La probabilité qu'il y ai moins de 40 piles est", b / 20, "%.")

l = []
for j in range(2000):
    l.append(pf())

plt.hist(l, bins=range(20, 80, 1))
plt.show()
