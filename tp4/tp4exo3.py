import matplotlib.pyplot as plt
import numpy as np

for t in np.arange(0.3,2,0.2):
    x = np.linspace(0,1,400);
    y = x**t
    plt.plot(x,y, label=t)

plt.legend(loc=0)
plt.figure()

i = 0

for t in np.arange(0.4,3,0.01):
    x = np.linspace(0,1,400);
    y = x**t
    plt.plot(x,y, color=plt.cm.hsv(i))
    i += 1


plt.title("mon bô graphique!!! :)")

plt.show()