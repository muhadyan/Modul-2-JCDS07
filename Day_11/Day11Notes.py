import numpy as np

# # Cari max dan minnya ada di index ke berapa
# x = [[4, 20, 3, 400, 5], [1, 5, 7, 9, 11]]
# y = np.array(x)

# print(np.argmax(y))
# print(np.argmin(y))



# # Matriks Identitas
# a = np.array([[1,2,3], [4,5,6]])
# b = np.array([[0,0,0], [0,0,0]])        # matriks identitasnya
# # atau bisa juga
# c = np.zeros((2, 3), dtype='int32')     # 2 dimensi berisi 3
# d = np.ones((2, 3), dtype='int32')      # angkanya 1 semua



# # 1 = True, 0 = False
# x = 0
# if x:
#     print(x)
# else:
#     print('y')

# x = np.zeros((3,3), dtype=bool)
# print(x)        # False semua

# x = np.ones((3,3), dtype=bool)
# print(x)        # True semua



# # Full
# lain = np.full((3,3), 1, dtype=bool)
# print(lain)     # Keluar True semua
# lain = np.full((3,3), 1)
# print(lain)     # Keluar 1 semua
# lain = np.full((3,3), 'Andi')
# print(lain)     # Keluar Andi semua



# # Mengubah array jadi list
# lain = np.full((3,3), 'Andi')
# print(lain.tolist())



# # Ngegabungin list
# x = [0,1,2,3,4]
# y = [5,6,7,8,9]
# ## Cara 1
# z = []
# z.append(x)
# z.append(y)
# print(z)

# ## Cara 2
# z = [x, y]
# print(z)

# ## Cara 3
# z = np.array(x+y).reshape(2, -1).tolist()
# print(z)

# ## Cara 4
# a = []
# a.extend(x)
# a.extend(y)
# z = np.array(a).reshape(2, -1).tolist()
# print(z)

# ## Cara 5
# xnp = np.array(x)
# ynp = np.array(y)
# z = np.concatenate([[xnp], [ynp]], axis=0).tolist()     # concat untuk menggabung 2 array jadi 1 array
# print(z)

# ## Cara 6
# z = np.vstack([xnp, ynp]).tolist()      # vstack = numpuk vertikal
# print(z)

# ## Cara 7
# z = np.r_[[xnp], [ynp]].tolist()
# print(z)

# ## Cara 8
# z = np.row_stack((xnp, ynp)).tolist()
# print(z)



# # Menumpuk array
# a = np.arange(6).reshape(2, -1)
# b = np.array([5,6,7,8,9,10]).reshape(2, -1)
# ## Vertikal
# c = np.vstack([a,b])
# print(c)
# d = np.concatenate([a,b], axis=0)
# print(d)
# e = np.row_stack((a,b))
# print(e)
# f = np.r_[a,b]
# print(f)

# ## Horizontal
# c = np.hstack([a,b])
# print(c)
# d = np.concatenate([a,b], axis=1)
# print(d)



# # Cari genapnya aja di array
# z = np.arange(1, 11)
# ## Cara 1 (slicing)
# print(z[1::2])

# ## Cara 2 (masukin condition)
# print(z[z % 2 == 0])



# # Mengubah yg ganjil jadi angka 0
# z = np.arange(1, 11)
# # Cara 1
# z[z % 2 != 0] = 0
# print(z)

# # Cara 2
# print(np.where(z % 2 != 0, 0, z))



# # Nyari range angka tertentu dalam sebuah array
# x = np.arange(10)
# print(x[np.where(x<6)])
# print(x[(x>4) & (x<8)])
# print(x[np.where((x>4) & (x<8))])
# print(x[np.where(np.logical_and(x>4, x<8))])



# # Determinan
# ## 2 x 2
# x = np.array([[3,1], [2,5]])
# print(np.linalg.det(x))

# ## 3 x 3
# y = np.array([[1,2,1], [3,3,1], [2,1,2]])
# print(np.linalg.det(y))



# # Invers
# z = np.array([[3,2], [1,4]])
# print(np.linalg.inv(z))

# # Matriks Identitas Umum (dot product)
# print(z@np.linalg.inv(z))
# print(z.dot(np.linalg.inv(z)))

# # Cross Product
# print(np.cross(z,z))



# # Tambahan
# # # Repeat
# print(np.repeat(1, 10))     # bikin array berisi angka 1 sebanyak 10 elemen
# a = np.array([1,2,3])
# print(np.repeat(a, 3))  # menduplikat isi array per elemen sebanyak 3 kali

# # # Tile
# a = np.array([1,2,3])
# print(np.tile(a,3))     # menduplikat isi array a sebanyak 3 kali

# # # Intersect1d
# a = np.array([1,2,3,2,3,4,3,4,5,6])
# b = np.array([7,2,10,2,7,4,9,4,9,8])
# np.intersect1d(a,b)     # mencari yg elemennya sama

# # Setdiff1d
# a = np.array([1,2,3,4,5])
# b = np.array([5,6,7,8,9])
# print(np.setdiff1d(a,b))