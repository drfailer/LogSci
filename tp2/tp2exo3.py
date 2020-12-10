import numpy as np
from math import factorial

def inverse(li):
    li.reverse()

def dec(b):
    s = 0
    cpt = 0
    inverse(b)
    for i in b:
        s += i * (2 ** cpt)
        cpt += 1

    return s

def len_bin(n):
    i = 0
    while n > 2 ** i:
        i += 1

    return i - 1

def binaire(n):
    bin = []
    try:
        # On peut utiliser le log2 pour récupérer la taille d'un nombre en binaire
        len = int(np.log2(n)) + 1
    except TypeError:
        # Si nombre trop grand
        len = len_bin(n)

    for i in range(len):
        bin.append((n >> i) % 2)
        
    inverse(bin)
    return bin

print(dec([1, 1, 0, 1]))
print(dec([1, 1, 0, 1, 1, 0, 0] + [1, 0, 1, 0, 1, 0, 1, 0]))
print(binaire(13))
print(binaire(dec([1, 1, 0, 1, 1, 0, 0]) + dec([1, 0, 1, 0, 1, 0, 1, 0])))
print(binaire(factorial(50)))
