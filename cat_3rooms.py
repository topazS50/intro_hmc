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

df = pd.DataFrame(data_pos)
df[:100].plot()
plt.savefig('cat_3rooms.jpeg')

grp = df.groupby(0)
df_count = grp.size()
print df_count/df_count[0]
