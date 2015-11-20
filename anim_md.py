import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import pandas as pd

data_x = pd.read_csv('hmc_md.csv', sep=' ', index_col=0)

fig = plt.figure()
ax = plt.axes(xlim=(-3, 3), ylim=(-0.1, 3))
line0,   = ax.plot([], [], lw=1)
points0, = ax.plot([], [], "o")
points1, = ax.plot([], [], "o")


def f(x):
#    return x * x
    return x * x * x * x - x * x


def init():
    x = np.linspace(-2, 2, 100)
    y = f(x)
    # print x
    # print y
    line0.set_data(x, y)
    return line0, points1


def animate(i):
    x = float(data_x['x'][i])
    y = f(x)
    points0.set_data(x, y)
    x = float(data_x['x0'][i])
    y = f(x)
    points1.set_data(x, y)
    return (points0, points1)

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=5100, interval=20, blit=True)
anim.save("hmc_2wel.mp4", fps=30)
# plt.show()
