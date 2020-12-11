import numpy as np
import matplotlib.pyplot as plt

# Constante :
N = 10


# La fonction f :
def f(x):
    return np.sin(x)


# Création de x :
x = np.linspace(-np.pi, np.pi, N+1) # x.shape = (4,)
x = x.reshape(N+1, 1)

# Création de L :
tmp = x
tmp.reshape(1, N+1)
L = np.ones((N+1, 1))
for i in range(1, N+1, 1):
    L = np.hstack((L, tmp**i))

# Création de b :
b = f(x)
b = b.reshape((N+1, 1))

# Création de a :
a = np.linalg.solve(L, b)

# Affichage avec polyfit :
x = x.reshape(N+1,)
Coef = [np.polyfit(x, f(x), i) for i in range(N+1)]
print(Coef)


# Création du graphe :
t = np.linspace(-np.pi, np.pi, 250)
plt.plot(t, f(t),linewidth=2, color='r')
plt.plot(t, np.polyval(a[::-1], t),linewidth=1, color='k')
plt.show()

# Observations :
# Avec N = 4, les courbes sont semblables (même variations) mais elles sont en décalé
# Avec N = 10, les courbes sont alignées donc plus N augmente plus P(x) se
# rapproche de f(x)
