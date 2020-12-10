import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1,4,1200)
y = 1/x
y1 = (-1/4)*(x-2)+1/2

plt.plot(x,y)
plt.plot(x,y1)

plt.show()