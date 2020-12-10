import numpy as np
import matplotlib.pyplot as plt


# Info sur fichier csv :
# Numero INSEE |  Nom |  Altitude |  Code postal |  Longitude |  Latitude |  Population(1999) |  Surface

# Coordonnées de Clermont-Ferrand :
longcf = 0.053843408089816
latcf = 0.79899719602977

# Listes pour valeurs :
lat_ = []
long_ = []
nom = []
code = []

# Récupération des données :
with open("./villes.csv", encoding="utf-8") as f:
    for i,line in enumerate(f):
        if i > 0:
            list_global = line.split(';')
            lat_.append(float(list_global[5]))
            long_.append(float(list_global[4]))
            nom.append(list_global[1])
            code.append(int(list_global[3][:2]))

# Retourne la distance entre deux point GPS proches :
def distance(long1, lat1, long2, lat2):
    c = 1.56961*10 ** (-4)
    return np.sqrt( (long1 - long2)**2 + (lat1 - lat2)**2 ) / c

# Récupération des villes du puys de dome et distance/clermont :
puys_dome = []
for i,c in enumerate(code):
    if c == 63:
        puys_dome.append([distance(long_[i], lat_[i], longcf, latcf), nom[i]])

puys_dome.sort()

# Ville la plus éloignée de clermont
plus_loin = max(puys_dome)
print("Ville la plus éloignée de clermont : ", plus_loin[1])
print("Elle est à une distance de :", plus_loin[0])

# Nombre de ville éloignée de R/2
d = plus_loin[0]/2
i = 0
while puys_dome[i][0] < d:
    i+=1


p = i / len(puys_dome)
print("Il y a ", 100*p, "% des villes éloignées de ", d)
