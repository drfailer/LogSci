import matplotlib.pyplot as plt
import numpy as np

co = []
cc = []
cma = []
cmi = []
dt = []
Acc = []

with open("cac40.csv", encoding="utf-8") as f:
    for ligne in f:
        ligne.replace(',','.')
        tabl = ligne.split(';')
        dt.append(tabl[1]);
        co.append(float(tabl[2]))
        cc.append(float(tabl[5]))
        cma.append(float(tabl[3]))
        cmi.append(float(tabl[4]))
       

        

##### 1

print("il y avait ",len(dt),"jours dans ce fichier");


##### 2
co_min = co[0]
min = 0
for i in range(1,len(co)):
    if(co_min > co[i]):
        co_min = co[i]
        min = i

print("Le cours d'ouverture le plus bas était en ",dt[i]);

##### 3

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


##### 4

print("La stratégie nous rapporte",strategie);

index = np.arange(2)
largeur = 0.4
plt.bar(index,infSup,largeur,color='b',label='inf|sup')

plt.ylabel('nbr de jour')
plt.title('comparaison inférieur/supérieur')

plt.legend()
plt.show()

## On observe que même si il y avait presque autant de jours avec un accroissement positif que négatif. Notre stratégie nous fait perdre 3000 euro. Ceci s'explque par le fait que les valeurs sont plus grandes lorsque c'est un jour négatif.
