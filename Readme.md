DEMO of HMC
=========

#### intro\_hmc\_2015\_11.pdf

presentation file at workshop.

#### cat\_3rooms.py

demonstration of MCMC with the cat in 3 rooms example.

Usage: python ./cat_3rooms.py

It return the ratio of probability to find a cat in each room. And generate a plot cat_3rooms.jpeg

#### mtpl.py anim\_mtpl.py

demonstration of Metropolis Algorithm with f(x) = x^2

Usage: python ./mtpl.py ; python ./anim_mtpl.py

mtpl.csv(data) and mtpl.mp4 are generated. 

In mtpl.mp4 'x' is previous point and 'o' are candidate. 

The distribution of sample are shown at the bottom as scattered 'x'.

#### hmc.py, anim\_hmc.py

demonstration of HMC with f(x) = x^2

Usage: python ./hmc.py ; python ./anim_hmc.py

hmc_md.csv(data) and hmc.mp4 are generated. 

In hmc.mp4 'x' is previous point and 'o' are candidate. 

The distribution of sample are shown at the bottom as scattered 'x'.

#### Requirements

python2.7, numpy, pandas, matplotlib, llmpeg and so on

#### TODO

tune the parameter for jpeg generation (it takes long)  

demonstration for more complecated f(x)

demonstration of leap frog integerator in clearer way

#### misc

HMC stands for Hybrid Monte Carlo or Hamiltonian Monte Carlo. (They are same.)

Lattice field theory people uses 'Hybrid', machine learning people uses 'Hamiltonian'.

Contact

https://www.facebook.com/kenji.ogawa.5209
