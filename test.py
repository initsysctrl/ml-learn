'''
Date: 2021-02-26 17:33:45
LastEditTime: 2021-03-01 02:46:04
Author: Ye-P
Descripttion: 
'''
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)
fig = plt.figure()
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid('-')
line, = plt.plot(x, y, color='black')


def init():  # only required for blitting to give a clean slate.
    line.set_ydata([np.nan] * len(x))
    return line,


def update(i):
    line.set_ydata(np.sin(x + i / 100))  # update the data.
    return line,


ani = animation.FuncAnimation(
    fig, update, init_func=init, interval=2, blit=True, save_count=50)

plt.show()
