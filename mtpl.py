'''
this calculates
Sum_i p_i v_i / Sum_i p_i
'''
import numpy as np
import pandas as pd


#
# \frac{\int dx exp(-x^2) (x^2)}{\int dx exp(-x^2)} = 0.5
#


def f(x):
    y = x * x
    return y


def df(x):
    dy = 2 * x
    return dy


def g(x):
    return x * x


# Number of Steps
MAX_COUNT = 10000
# parameter of step
EPS = 0.5

# Initial state
x = np.random.uniform(-1.0, 1.0)

# store value of x's
sequence = np.asarray([])

data_x = []

doIter = True
count = 0
while (doIter):
    x_trial = x + np.random.normal() * EPS
    data_x.append([x_trial, x])
    z = np.exp(-f(x))
    z_trial = np.exp(-f(x_trial))
    if z_trial > z:
        x = x_trial
    else:
        rnd = np.random.random()
        if rnd < z_trial / z:
            x = x_trial

    sequence = np.append(sequence, x)
    if count > MAX_COUNT:
        doIter = False
    count += 1

pd.DataFrame(data_x, columns=['x_trial','x']).to_csv('mtpl.csv', sep=' ')
estimate = np.asarray([g(x) for x in sequence]).mean()
print estimate
