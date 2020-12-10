import sympy as sm
import numpy as np
from scipy.integrate import quad

# Fonctions :
def f(x):
    return np.exp(np.sin(x))

def g(x):
    return np.exp(-(x**2))



# Méthode des rectangles à fauche
def int_rectg(f, a, b, n):
    xi = np.linspace(a, b, n+1)
    h = (b - a)/n
    yi = list(map(f, xi[:n]))
    return h * sum(yi)

# Méthode des rectangle à droite
def int_rectd(f, a, b, n):
    xi = np.linspace(a, b, n+1)
    h = (b - a)/n
    yi = list(map(f, xi[1:n+1]))
    return h * sum(yi)

# Méthode des trapèzes
def int_trap(f, a, b, n):
    xi = np.linspace(a, b, n+1)
    h = (b - a)/n
    yi = list(map(f, xi))
    return h * ((yi[0] + yi[n])/2 + sum(yi[1:n]))

# Question 1
print("Sg =", int_rectg(np.sin, 0, np.pi/2, 100))
print("Sd =", int_rectd(np.sin, 0, np.pi/2, 100))
print("St =", int_trap(np.sin, 0, np.pi/2, 100))

# Question 2
for i in range(7, 8, 1):
    nb_rect = 10**i
    print("Pour ", nb_rect, "rectangles:")
    print("Valeurs pour f:")
    print("Sg =", int_rectg(f, -np.pi, np.pi, nb_rect))
    print("Sd =", int_rectd(f, -np.pi, np.pi, nb_rect))
    print("St =", int_trap(f, -np.pi, np.pi, nb_rect))
    print("Valeurs pour g:")
    print("Sg =", int_rectg(g, -10, 2, nb_rect))
    print("Sd =", int_rectd(g, -10, 2, nb_rect))
    print("St =", int_trap(g, -10, 2, nb_rect))
# Résultats
# Pour f: 7.954926521012877
# Pour g: 1.768307217188941
# Les résultats trouvé par les méthode sont plus proches quand nb_rect grandi
# Pour avoir un résultat précis, il faut donc faire les calcules avec beaucoup
# de rectangles

# Question 3
print("Résultats avec quad")
print(quad(f, -np.pi, np.pi))
print(quad(f, -10, 2))
# on constate une différence de résultat pour g
