import numpy as np
from scipy.fft import fft
from wave_shown import *
import matplotlib.pyplot as plt

# Number of sample points
N = 400
# sample spacing
T = 1.0 / 800.0
frequencies = [1, 30, 40, 50, 75, 125]
x = np.linspace(0.0, N*T, N)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)

# for f in frequencies:
f = 125
w = 2.0*np.pi*f
# y = asymSin(2 * w * x)
# y = ramp(2 * w * x)
# y = step(2 * w * x)
# y = twoStep(2 * w * x)
y = threeToOne(4 * w * x)
yf = fft(y)

# plt.plot(x, y)
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()
plt.show()
