import numpy as np
import matplotlib.pyplot as plt


# Test si un mouvement est correcte (si le cavalier reste sur le plateau) :
def verification(a,b):
    c = [x+y for x,y in zip(a,b)]
    if -1 in c or -2 in c or 8 in c or 9 in c:
        return False
    return True

# Retourne un mouvement valide :
def un_pas(l):
    mouvement = [[ 1,  2],
                 [ 1, -2],
                 [-1,  2],
                 [-1, -2],
                 [ 2,  1],
                 [ 2, -1],
                 [-2,  1],
                 [-2, -1]]
    
    i = 1
    while i == 1:
        
        alea = np.random.randint(8)
        
        if(alea == 0 and verification(l,mouvement[0])):
            l  = [x + y for x,y in zip(l,mouvement[0])]
            i = 0
        elif(alea == 1 and verification(l,mouvement[1])):
            l  = [x + y for x,y in zip(l,mouvement[1])]
            i = 0
        elif(alea == 2 and verification(l,mouvement[2])):
            l  = [x + y for x,y in zip(l,mouvement[2])]
            i = 0
        elif(alea == 3 and verification(l,mouvement[3])):
            l  = [x + y for x,y in zip(l,mouvement[3])]
            i = 0
        elif(alea == 4 and verification(l,mouvement[4])):
            l  = [x + y for x,y in zip(l,mouvement[4])]
            i = 0
        elif(alea == 5 and verification(l,mouvement[5])):
            l  = [x + y for x,y in zip(l,mouvement[5])]
            i = 0
        elif(alea == 6 and verification(l,mouvement[6])):
            l  = [x + y for x,y in zip(l,mouvement[6])]
            i = 0
        elif(alea == 7 and verification(l,mouvement[7])):
            l  = [x + y for x,y in zip(l,mouvement[7])]
            i = 0

    return l

# Retourne le nombre de pas effectues pas le cavalier pour revenir à son point
# de départ :
def excursion(d):
    i = 1
    depart = d
    d = un_pas(d)
    while (d != depart):
        d = un_pas(d)
        i += 1
       
    return i

# Affiche dans chaque cases de coup le nombre moyen de pas effectues lors de
# l'excursion du cavalier en partant de cette même case :
coup = np.zeros((8,8))
for i in range(64):
    for _ in range(2000):
        coup[i//8][i%8] += excursion([i//8,i%8])
    print(i//8,i%8,coup[i//8][i%8])
    coup[i//8][i%8] /= float(2000)
    print( coup[i//8][i%8])

plt.matshow(coup)
plt.show()
