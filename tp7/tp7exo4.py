import numpy as np
def serie(n):
    return np.random.randint(1,7,size = n)


print(serie(10))
p = 0
p2 = 0

for i in range(2000):
    for i in serie(4):
        if i == 6:
            p += 1
    for i in range(24):
        A = serie(24)
        B = serie(24)
        if(A[i] == 6 and B[i] == 6):
            p2 += 1
        
    
           
print("la probabilité d'obtenir un 6 après 4 lancer est donc de",float(p/2000), "est la probabilité d'avoir 2 6 en 24 lancer et de",float(p2/2000))

