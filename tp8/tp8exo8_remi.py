import numpy as np

# Précision
sigma = 10**(-8)

# Fonctions
def f(x):
    return np.log(x) - np.sin(x)

def df(x):
    return 1/x - np.cos(x)

def g(x):
    return 2*x + 3 - np.exp(x)

def dg(x):
    return 2 - np.exp(x)


# Calcule de l'aire avec la méthode de Newton :
def newt(f, df, x, esp):
    i = 0
    xn = x
    while np.absolute(f(xn)) > esp:
        i += 1
        xn1 = xn - (f(xn)/df(xn))
        xn = xn1

    return xn, i

print(newt(f, df, 1, sigma))
print(newt(g, dg, 0, sigma))
