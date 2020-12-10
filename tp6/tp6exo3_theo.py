import numpy as np

def compo2(couple):
    return couple[1]

# Listes :
insee = []
nom = []
altitude = []
codePostal = []
longitude_rad = []
latitude_rad = []
pop = []
surface = []

# Récupération des données :
with open("./villes.csv", encoding="utf-8") as f:
    for num,line in enumerate(f):
        if num != 0:
            list = line.split(';')
            insee.append(list[0])
            nom.append(list[1])
            altitude.append(int(list[2]))
            #codePostal.append(int(list[3]))
            longitude_rad.append(float(list[4]))
            latitude_rad.append(float(list[5]))
            pop.append(float(list[6]))
            surface.append(float(list[7]))

indiceVilleDans63 = []
for indice, valeur in enumerate(insee):
    if(valeur.startswith("63")):
       indiceVilleDans63.append(indice)

rad_to_km = 6371.009359
lon_cf = 0.053843408089816
lat_cf = 0.79899719602977
coupleVilleDistance = []

for i in indiceVilleDans63:
    coupleVilleDistance.append([nom[i],float(np.sqrt(np.power(lon_cf -longitude_rad[i],2)+np.power(lat_cf - latitude_rad[i],2))*rad_to_km)])

coupleVilleDistance.sort(key=compo2)

## 1
for i in range(30):
    print(coupleVilleDistance[i])


## 2 & 3
print("La commune la plus éloigné de Clermont dans le puy de dôme est",coupleVilleDistance[len(coupleVilleDistance)-1][0], "qui se situe à plus de",coupleVilleDistance[len(coupleVilleDistance)-1][1], "km")

