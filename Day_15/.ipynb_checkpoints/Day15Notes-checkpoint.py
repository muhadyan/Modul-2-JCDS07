import pandas as pd
import numpy as np

# # Replace (bisa juga dipake buat NaN)
# ## Single Replace
# df = pd.read_csv('data.csv')
# df = df.replace('-', 0)
# print(df)

# ## Multiple Replace
# df = pd.read_csv('data.csv')
# df = df.replace(['-', '#'], 0)
# print(df)

# ## Ngeubah jadi NaN
# df = pd.read_csv('data.csv')
# df = df.replace(['-', '#'], np.NaN)
# df = df.fillna('xxx')
# print(df)

# ## yg '-' diganti jadi '+', sedangkan yg '#' diubah jadi NaN
# df = pd.read_csv('data.csv')
# df = df.replace({
#     '-': '+',
#     '#': np.NaN
# })
# print(df)

# ## yg '-' di kolom usia diubah jadi NaN
# df = pd.read_csv('data.csv')
# df = df.replace({
#     'usia': '-'
#     }, np.NaN)
# print(df)

# ## yg '-' dan '#' di kolom usia diubah jadi NaN
# df = pd.read_csv('data.csv')
# df = df.replace({
#     'usia': ['-', '#']
#     }, np.NaN)
# print(df)

# ## yg '-' dan '#' di kolom usia serta '#' di kolom nama diubah jadi NaN
# df = pd.read_csv('data.csv')
# df = df.replace({
#     'usia': ['-', '#'],
#     'nama': '#'
#     }, np.NaN)
# print(df)

# ## yg '-' dan '#' di kolom usia diubah jadi NaN serta '#' di kolom nama diubah jadi 'Anonim'
# df = pd.read_csv('data.csv')
# df = df.replace({
#     'usia': ['-', '#'],
#     'nama': '#'
#     }, {
#         'usia': np.NaN,
#         'nama': 'Anonim'
#     })
# print(df)


# ## Forward Filling
# df = pd.read_csv('data.csv')
# df['usia'] = df['usia'].replace(
#     to_replace = '-',
#     method = 'ffill'
# )
# print(df)

# ## Backward Filling
# df = pd.read_csv('data.csv')
# df['usia'] = df['usia'].replace(
#     to_replace = '-',
#     method = 'bfill'
# )
# print(df)