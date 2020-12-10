import numpy as np
import matplotlib.pyplot as plt


plt.hist([np.sin(i) for i in np.arange(1000)], np.arange(-1, 1, 0.1))
plt.show()

# On peut voir sur la graphique que la repartition n'est pas uniforme
