import matplotlib.pyplot as plt
import numpy as np

# Création de la liste nbr_occ de la façon suivante :
# [['A', 0], ['B', 0], ..., ['Z', 0]]
nbr_occ = []
for i in np.arange(26):
    nbr_occ.append([chr(ord('A') + i), 0])

# Récupération des lignes et comptage des lettres :
with open("./sherlock.txt", encoding="utf-8") as f:
    for line in f:
        line.upper() # Lettres en majuscules
        for c in line:
            nbr_occ[ord(c)%26][1] +=1

# tri de la liste selon le deuxieme paramètre
nbr_occ = sorted(nbr_occ, key=lambda x: x[1])

# Construction du diagramme en battons :
lettres = []
chiffres = []
for i in nbr_occ:
    lettres.append(i[0])
    chiffres.append(i[1])

largeur = 0.35
plt.bar(lettres, chiffres, largeur, color='r')
plt.show()
