import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

t = np.linspace(0,5,100)
g = np.zeros(100)

fig, axs = plt.subplots(3, sharex=True, sharey=False)

axs[0].plot(t, g - 9.8, color='black')
axs[1].plot(t, (-9.8*t), color='black')
axs[2].plot(t, (-9.8*t**2+100), color='black')

axs[2].set_xlabel('time [s]')
axs[0].set_ylabel(r'a(t) $m/s^2$')
axs[1].set_ylabel(r'v(t) $m/s$')
axs[2].set_ylabel(r'x(t) $m$')

axs[0].set_ylim(-15,15)
axs[1].set_ylim(-50,10)
axs[2].set_ylim(-150,150)

#figure = Figure(figsize=(6, 5))
plt.savefig('/Users/sahagunjaime/Desktop/prob5.png')


