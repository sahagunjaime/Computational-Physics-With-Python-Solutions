import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


N, t = np.loadtxt('/Users/sahagunjaime/Desktop/data.txt', unpack=True)

L= np.log(2)/170
N_0=29250

plt.title('Ba137 Decay')
plt.xlabel('time [s]')
plt.ylabel('N')

plt.grid(color='black', linestyle='-', linewidth=.1)
plt.plot(t, N, color='black', label='Ba137 data')
plt.plot(t, N_0*np.exp(-L*t), color='red', label='approx.')
plt.legend(loc='best')

figure = Figure(figsize=(6, 5))
plt.show()
