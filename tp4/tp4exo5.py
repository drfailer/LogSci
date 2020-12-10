import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0,2*np.pi,400)
x = np.cos(t)
y = np.sin(t)

plt.plot(x,y)
plt.plot([0,np.cos(7*np.pi/6),np.cos(-np.pi/6),0],[1,np.sin(7*np.pi/6),np.sin(-np.pi/6),1])
plt.axis("equal")
plt.show()
