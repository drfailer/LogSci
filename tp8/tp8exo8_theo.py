import numpy as np

def sin(x):
    return np.sin(x)
    
def dsin(x):
    return np.cos(x)

# Calcule de l'aire sous la courbe de f à l'aide de la méthode de Newton :
def newt(f,df,x,eps):
    i = 0
    while(abs(f(x)) >= eps):
        x = x-f(x)/df(x)
        i+=1
    return i,x


a,b = newt(sin,dsin,2,0.00000000002)
print(a,b)
