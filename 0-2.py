import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

N, t = np.loadtxt('/Users/sahagunjaime/Desktop/data.txt', unpack=True)

fig, axs = plt.subplots(2)

fig.suptitle('Ba137 Decay')
axs[0].plot(t, N, color='black')
axs[1].plot(t, np.log(N), color='black')

axs[0].set_ylabel('N')
axs[1].set_ylabel('log(N)')
axs[1].set_xlabel('time [s]')


figure = Figure(figsize=(6, 8))

plt.show()
