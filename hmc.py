'''
this calculates
'''
import numpy as np
import pandas as pd

def f(x) :
    y = x * x
    return y

def df(x) :
    dy = 2 * x
    return dy

def step_leapfrog( x , p , dtau ) :
    dp = - df( x )
    p = p + dp * dtau * 0.5
    x = x + p * dtau
    dp = - df( x )
    p = p + dp * dtau * 0.5
    return x , p

def molecdyn ( x , p , dtau , nsteps , data) :
    x0 = x
    data.append([0, x, x0])
    for ii in range ( nsteps ) :
        x , p = step_leapfrog ( x , p , dtau )
        data.append([ii+1, x, x0])
    return x , p


MAXITER=10000
data_md = []
dtau = 0.01
nsteps = 50
x = np.random.uniform(-1.0,1.0)
sequence = np.asarray([])
doIter = True
count = 0
while ( doIter ) :
    p = np.random.normal( scale = 1.0 )
    h = f(x) + 0.5 * p * p
    x_trial , p = molecdyn ( x , p , dtau , nsteps, data_md )
    h_trial = f( x_trial ) + 0.5 * p * p
    z = np.exp( - h )
    z_trial = np.exp( - h_trial )
    #print "h" , h , h_trial
    if z_trial > z :
        x = x_trial
    else :
        rnd = np.random.random()
        if rnd < z_trial / z :
            x = x_trial

    sequence = np.append( sequence , x )
    if count > MAXITER:
        doIter = False
    count += 1

pd.DataFrame(data_md,columns=['step','x','x0']).to_csv('hmc_md.csv',sep=' ')

#print sequence[:100]

estimate = (sequence*sequence).mean()
print '<x^2>/<1>', estimate
