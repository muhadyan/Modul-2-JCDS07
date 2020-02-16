import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'x': [1,2,3,4,5],
    'y': [9,5,7,3,6],
    'z': [2,3,4,5,3]
})
# # Figure
# plt.style.use('seaborn')
# plt.figure('Tes')
# plt.plot(df['x'], df[['y', 'z']])
# plt.grid(True)
# plt.show()



# # Multifigure
# plt.figure('Tes')

# # plot 1 kiri
# plt.subplot(331)
# plt.plot([1,2,3], [4,5,6])
# plt.title('Tes 1')

# # plot 2 kanan
# plt.subplot(336)
# plt.plot([1,2,3], [3,2,1])
# plt.title('Tes 1')
# plt.suptitle('Tes 1 dan 2')


# plt.figure('Tes2')

# # plot 1 kiri
# plt.subplot(331)
# plt.plot([1,2,3], [4,5,6])
# plt.title('Tes 1')

# # plot 2 kanan
# plt.subplot(336)
# plt.plot([1,2,3], [3,2,1])
# plt.title('Tes 1')
# plt.suptitle('Tes 1 dan 2')

# plt.grid(True)
# plt.show()