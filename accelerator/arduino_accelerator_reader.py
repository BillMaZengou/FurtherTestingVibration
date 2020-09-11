import serial
import time
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt

serialPort = "/dev/cu.usbmodem141401"  # check the port
baudRate = 115200   # may modify
ser = serial.Serial(serialPort, baudRate, timeout=None)

x = []
y = []
z = []
t = []

start_time = time.time()
i = 0
while i < 1000:
    if i % 10 == 0:
        print("Now is step {}".format(i))
    str = ser.readline()
    output = str.split()
    if len(output) > 0:
        output = output[0].decode("utf-8").split(",")
        x.append(float(output[0]))
        y.append(float(output[1]))
        z.append(float(output[2]))
        t.append(time.time()-start_time)
    i += 1
ser.close()

x = np.array(x)
y = np.array(y)
z = np.array(z)
t = np.array(t)


data = np.column_stack((t, x, y, z))
header = "Time, X-Column, Y-Column, Z-Column"
np.savetxt('./resonance/test_150.txt', data, header=header)

# fig1, ax = plt.subplots()
# line1 = ax.plot(t, y, '-b', label="Real-time Position")
# line2 = ax.plot(t, np.ones_like(t)*mean_y, '--r', label="Average Position")
# line3 = ax.plot(t, np.ones_like(t)*ground_y, '--k', label="Equalibrium Position")
# # print(mean_y)
# ax.legend(loc='upper right')
# ax.set_title('Longitudinal Vibration')
#
# fig, axs = plt.subplots(1, 2)
# axs[0].plot(t, x, '-k')
# axs[0].set_title('X-axis Movement')
# axs[1].plot(t, z, '-k')
# axs[1].set_title('Z-axis Movement')
# plt.show()
