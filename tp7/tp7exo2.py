import numpy as np
import matplotlib.pyplot as plt

# Retourne 100 lancé :
def piece():
    return np.random.randint(2,size = 100)

# Retourne le nombre de suite de k piles dans L:
def suitePile(a,b):
    L = [0] * (b-a+1)
    nbrDePile = 0
    
    for i in piece():
        if i == 1:
            nbrDePile += i
            for i in range(len(L)):
                if(nbrDePile == i+a):
                    L[i] = 1
        else:
            nbrDePile = 0    
            
    return L


# Calcule des probabilités :
proba = [0] * 6
for i in range(2000):
    proba = [a + b for a, b in zip(proba, suitePile(3,8))]
    
    
print("il y a une probabilité de",float(proba[1]/2000),"d'avoir 4 pile d'affilé dans une série de 100 lancer")

proba[:] = [x / 2000 for x in proba]

# Construction du graphe :
index = np.arange(6);
largeur = 0.8
plt.bar(index,proba,largeur,color = 'b')
plt.xlabel('nombre de pile à la suite')
plt.ylabel('probabilité')
plt.xticks(index,[i for i in range(3,9)])

plt.legend
plt.show()
