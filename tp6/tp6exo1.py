############################################################
#                         cac40                            #
############################################################
import matplotlib.pyplot as plt
import numpy as np


############################################################
# Listes :
co = []
cc = []
cma = []
cmi = []
dt = []
Acc = []

# Récupération des données
with open("./resources/cac40.csv", encoding="utf-8") as f:
    for ligne in f:
        ligne.replace(',','.')
        tabl = ligne.split(';')
        dt.append(tabl[1]);
        co.append(float(tabl[2]))
        cc.append(float(tabl[5]))
        cma.append(float(tabl[3]))
        cmi.append(float(tabl[4]))

############################################################


# Question 1 :
# nombre de jours
print("il y avait ",len(dt),"jours dans ce fichier");


# Question 2 :
# Date du cours d'ouverture le plus bas
# BUG:
co_min = co[0]
min = 0
for i in range(1,len(co)):
    if(co_min > co[i]):
        co_min = co[i]
        min = i

# Deux résultats differents
print("Le cours d'ouverture le plus bas était en ",dt[i])
print("Le cours d'ouverture le plus bas était en ",dt[np.argmin(co)])

# Question 3
# Accroissement journalier entre la cloture et la fermeture
infSup = [0,0]
strategie = 0

for i in range(len(cc)):
    Acc.append(cc[i]-co[i])
    if(cc[i]-co[i] < 0):
        infSup[0] += 1
    else:
        infSup[1] +=1
    strategie += cc[i]-co[i]
        

    
#### plt.plot(Acc)
#### plt.show()


# Question 4 :
# Stratégie: achat à l'ouverture et vente à la cloture
print("La stratégie nous rapporte",strategie);

index = np.arange(2)
largeur = 0.4
plt.bar(index,infSup,largeur,color='b',label='inf|sup')

plt.ylabel('nbr de jour')
plt.title('comparaison inférieur/supérieur')

plt.legend()
plt.show()

# On observe que même si il y avait presque autant de jours avec un
# accroissement positif que négatif. Notre stratégie nous fait perdre 3000
# euro. Ceci s'explque par le fait que les valeurs sont plus grandes lorsque
# c'est un jour négatif.
