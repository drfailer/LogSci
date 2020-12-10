import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 400)
y = x**2
plt.plot(x, y)
plt.plot(x, 4 - x**2)
plt.axis("equal")
plt.figure()

x1 = np.linspace(-10,10,400)
y1 = np.sin(x1)/x1
plt.plot(x1,y1)

plt.figure()

x2 = np.linspace(0,20,400)
y2 = np.sin(x2**2)
plt.plot(x2,y2)



plt.show()
