import matplotlib.pyplot as plt
import numpy as np

x = [0,0]
y = [2,0]
z = [1,1]

for i in range(10):
    plt.plot([x[0],y[0],z[0],x[0]],
             [x[1],y[1],z[1],x[1]])
    tempo = x
    x = [(x[0]+y[0])/2,(x[1]+y[1])/2]
    y = [(z[0]+y[0])/2,(z[1]+y[1])/2]
    z = [(z[0]+tempo[0])/2,(z[1]+tempo[1])/2]
plt.show()
