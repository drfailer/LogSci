def pgcd(a, b):
    if a > b:
        c = b
        b = a
        a = c

    while b % a !=0:
        r = b % a
        b = a
        a = r

    return a


def phi(n):
    s = 0
    for k in range(1, n + 1, 1):
        if pgcd(k, n) == 1:
            s += 1

    return s


def farey(n):
    s = 0
    for j in range(1, n + 1, 1):
            for k in range(1, j+1, 1):
                # Invariant: on vérifie que k/j est irréductible et on
                # incrémente s de 1 si oui et on a k <= j
                if pgcd(k, j) == 1:
                    s += 1

    return s + 1 # on ajoute 1 pour prendre en compte le 0/1

# Question 1
print('pgcd(123456, 234567) = ', pgcd(123456, 234567))

# Question 2
print(phi(10))
print(phi(30))

# Question 3
print(farey(4))
print(farey(10), farey(30))
