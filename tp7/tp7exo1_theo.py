import numpy as np
import matplotlib.pyplot as plt
def piece():
    return np.random.randint(2,size = 100)


def pf():
           
    pile = 0
    
    for i in piece():
        pile += i  
    return pile

sup,inf = 0,0
proba = [0] * 101

for i in range(2000):
    p = pf()
    if p > 53 :
        sup += 1
    elif p <= 40 :
        inf += 1
    proba[p] += 1

print("On a donc une probabilité de ", float(sup/2000), "d'avoir plus de 53 pile et une probabilité de",float(inf/2000),"d'avoir moins de 40 pile sur 100 lancer")
        
proba[:] = [x / 2000 for x in proba]
index = np.arange(101);
largeur = 0.8
plt.bar(index,proba,largeur,color = 'b')
plt.xlabel('nombre de pile')
plt.ylabel('probabilité')
plt.xticks(index,[i for i in range(101)])

plt.legend
plt.show()
