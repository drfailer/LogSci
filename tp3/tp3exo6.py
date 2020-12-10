import  numpy as np
import math
import matplotlib.pyplot as plt

def triangle(x, y, c):
    plt.fill([x, x+c, x+c/2], [y, y, y+c*np.sqrt (3)/2] , "r")




def t2s(n,x,y,c):
    if n == 0:
        triangle(x,y,c)
        triangle(x+c,y,c)
        triangle(x+c/2,y+math.sqrt(3)*c/2,c)

    else:
        t2s(n-1,x,y,c/2)
        t2s(n-1,x+c,y,c/2)
        t2s(n-1,x+c/2,y+math.sqrt(3)*c/2,c/2)

t2s(6,-10,-10,0.5)
plt.show()
