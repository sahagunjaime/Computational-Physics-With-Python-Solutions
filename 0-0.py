import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


x = np.linspace(0,5,100)

plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(0, 5)
plt.ylim(-.2, .5)

plt.plot(x, x**4 * np.exp(-2*x), color='red', label='first')
plt.plot(x, (x**2 * np.exp(-x) * np.sin(x**2))**2, color='black', label='second')
plt.legend(loc='upper right')

figure = Figure(figsize=(6, 5))
plt.show()
