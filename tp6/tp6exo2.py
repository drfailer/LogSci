import numpy as np
import matplotlib.pyplot as plt


point_median = []

# Calcule la distance entre deux points gps
def distance(x, y):
    c = [0, 0]
    c[0] = x - point_median[0]
    c[1] = y - point_median[1]
    return np.sqrt(c[0]**2 + c[1]**2)

############################################################################################
# Trouver la ville la plus au nord
def plus_nord(nom, latitude):
    maxi = 0
    ville_nord = []
    for i,j in enumerate(nom):
            if np.abs(np.pi/2 - latitude[i]) < np.abs(np.pi/2 - maxi):
                maxi = latitude[i]
                ville_nord = j

    print(ville_nord)
    
############################################################################################
# Latitude mediane
def lat_med(latitude):
    temp = latitude[:]
    temp.sort()
    point_median.append(temp[len(temp)//2])
    temp = longitude[:]
    temp.sort()
    point_median.append(temp[len(temp)//2])
    print(point_median[0])
    print(point_median[1])

############################################################################################
# Commune la plus proche du point mediant
def plus_proche_point_med(nom, longitude, latitude):
    plus_proche = [0, 0]
    commune = ''
    for i,j in enumerate(nom):
        point = [latitude[i], longitude[i]]
        if distance(point[0], point[1]) < distance(plus_proche[0], plus_proche[1]):
            plus_proche[:] = point[:]
            commune = j

    print(commune)

############################################################################################
# Histogramme de la population des communes (population comprise entre 1000 et 2000)
def histo(pop):
    plt.hist(pop, bins=np.arange(950, 20050, 100), edgecolor='black')
    plt.show()

############################################################################################
# affichage des villes de plus de 100 000 hab
latitude_tmp1 = []
longitude_tmp1 = []
latitude_tmp2 = []
longitude_tmp2 = []
def plus_cent_mille(latitude, longitude, pop, nom):
    for i,j in enumerate(pop):
        if j > 100000:
            latitude_tmp1.append(latitude[i])
            longitude_tmp1.append(longitude[i])
            print(nom[i])
        else:
            latitude_tmp2.append(latitude[i])
            longitude_tmp2.append(longitude[i])            

    plt.plot(longitude_tmp2, latitude_tmp2, linestyle='none', marker='o', c='b')
    plt.plot(longitude_tmp1, latitude_tmp1, linestyle='none', marker='o', c='r')
    plt.show()

############################################################################################
# main:
nom = []
longitude = []
latitude = []
pop = []
with open("./villes.csv", encoding="utf-8") as f:
    for i,line in enumerate(f):
        if i != 0:
            list = line.split(';')
            nom.append(list[1])
            longitude.append(float(list[4]))
            latitude.append(float(list[5]))
            pop.append(int(list[6]))
    lat_med(latitude)
    plus_nord(nom, latitude)
    plus_proche_point_med(nom, latitude, longitude)
    histo(pop)
    plus_cent_mille(latitude, longitude, pop, nom)


############################################################################################
# Agglomeration
def agglomeration(nom):
    with open("./villes.csv", encoding="utf-8") as f:
        for j, line in enumerate(f):
            if j != 0:
                list = line.split(';')
                if list[1] == nom:
                    coord = [float(list[5]), float(list[4])]
                    for i, l in enumerate(f):
                        if i != 0:
                            lst = l.split(';')
                            y = (coord[0]) - (float(lst[5]))
                            x = (coord[1]) - (float(lst[4]))
                            if np.sqrt(x**2 + y**2) <= 20 * 1.56961 * 10**(-4):
                                print(lst[1])

print('Agglomeration:\n')
agglomeration('Clermont-Ferrand')
