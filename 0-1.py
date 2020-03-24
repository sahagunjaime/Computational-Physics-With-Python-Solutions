import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

f,m1,m2 = np.loadtxt('/Users/sahagunjaime/Desktop/microphone.txt', unpack=True)

plt.xlabel('Frequency [Hz]')
plt.ylabel(r'Amplitude Ratio [$Mic_2/Mic_1$]')

plt.plot(f, m2/m1, color='red')

plt.show()
