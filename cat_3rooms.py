import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


NITER = 100000
pos = 0
transition = [[0, 1, 0], [1./6, 1./3, 1./2], [0, 1./2, 1./2]]

data_pos = []
for i in range(NITER):
    pos_next = np.random.choice([0, 1, 2], p=transition[pos])
    pos = pos_next
    data_pos.append(pos)

df = pd.DataFrame(data_pos, columns=['location of the cat'], index = None)
df[:100].plot(style='-o', ylim=[-0.1, 2.1])
plt.savefig('cat_3rooms.jpeg')

grp = df.groupby('location of the cat')
df_count = grp.size()

df_ratio = pd.DataFrame(df_count.get_values()/float(df_count.get_values()[0]), columns = ['ratio of counts'], index = ['room I','room II','room III'])
print df_ratio
