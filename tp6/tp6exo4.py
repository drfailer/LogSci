import matplotlib.pyplot as plt
import numpy as np

nbr_occ = []
for i in np.arange(26):
    nbr_occ.append([chr(ord('A') + i), 0])

with open("./sherlock.txt", encoding="utf-8") as f:
    for line in f:
        line.upper()
        for c in line:
            nbr_occ[ord(c)%26][1] +=1

# tri de la liste selon le deuxieme parametre
nbr_occ = sorted(nbr_occ, key=lambda x: x[1])

lettres = []
chiffres = []
for i in nbr_occ:
    lettres.append(i[0])
    chiffres.append(i[1])

largeur = 0.35
plt.bar(lettres, chiffres, largeur, color='r')
plt.show()
