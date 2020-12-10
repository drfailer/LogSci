def carree_plus(n):
    b = n*n+2
    return b
    print("Ceci ne sert à rien")

def racine(a,b,c):
    d = b ** 2 - 4 * a * c
    s = 0
    if d > 0:
        s = 2
    elif d == 0:
        s = 1

    return s

print(carree_plus(345) + carree_plus(567))
print(racine(1, 1, -2), racine(4, -12, 9), racine(2, 1, 1))