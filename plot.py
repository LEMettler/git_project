import numpy as np
import matplotlib.pyplot as plt

x, y = np.loadtxt('Values.txt', unpack=True)


plt.plot(x, y, 'r')
plt.show()
