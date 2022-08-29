import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

x = np.arange(0, 200, 0.2)
y = np.sin(x)

plt.plot(x, y)
plt.show()
