import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d

df = pd.read_excel('indo_12_1.xls', header=3, index_col=0, skipfooter=3, na_values='-')

fig = plt.figure(figsize=[15,5])
p = plt.subplot(111, projection='3d')

for j in df:
    for i in df:
        x = np.arange(len(df[i]))
        y = i
        z = np.zeros(len(df[i]))
        dx = np.ones(len(df[i]))
        dy = np.ones(len(df[i]))
        dz = df[i]
        p.bar3d(x, y, z, dx, dy, dz)


plt.xticks(np.arange(len(df.index)), df.index, rotation=90)
# plt.yticks(np.arange(len(list(df))), list(df), rotation=45)

p.set_zlabel('Sumbu Z')
plt.show()