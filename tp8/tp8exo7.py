import numpy as np

# Précision
sigma = 10**(-8)

# Fonctions
def f1(x):
    return np.log(x) - np.sin(x)

def f2(x):
    return 2*x + 3 - np.exp(x)


# Fonction de dichotomie
def dicho(f, a, b, esp):
    x = (a + b)/2
    while np.absolute(f(x)) > esp:
        if f(x) < 0:
            a = (a + b)/2
        else:
            b = (a + b)/2
        x = (a + b)/2
    
    return x

print(dicho(f1, 2, 10, sigma))
print(dicho(f2 , -10, 10, sigma))

# Fonction de dichotomie qui retourne le nombre de tours
def dicho_nbr(f, a, b, esp):
    x = (a + b)/2
    i = 0
    while np.absolute(f(x)) > esp:
        i += 1
        if f(x) < 0:
            a = (a + b)/2
        else:
            b = (a + b)/2
        x = (a + b)/2
        
    return i


print(dicho_nbr(f1, 1, 10, sigma))
print(dicho_nbr(f2 , -10, 10, sigma))
