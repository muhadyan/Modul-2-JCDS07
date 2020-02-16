import numpy as np
# # 1 Dimensi
# x = [1, 2, 3, 4, 5]
# y = np.array(x)     # Tuple berubah jadi array juga. Set berubah jadi array juga tapi tetep kurung {}

# print(x)    # pake koma
# print(y)    # tanpa koma (matriks)

# print(y.ndim)   # buat tau ada berapa dimensi

# print(x[0])
# # hasilnya sama kayak
# print(y[0])



# # 2 Dimensi
# x = [[1, 2, 3], [4, 5, 6]]
# y = np.array(x)

# print(x)
# print(y)    # langsung jadi matriks

# print(y[1, 1])  # sama dengan y[1][1]



# # 3 Dimensi
# z = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
# z = np.array(z)

# print(z)
# print(z.ndim)
# print(z.size)       # ngecek banyak isinya
# print(z.dtype)      # ngecek type isinya
# print(z.itemsize)   # ngecek besar byte nya
# print(z.shape)      # (1, 3, 3) dimensi 1 ada 1 elemen, dimensi 2 ada 3 elemen, dimensi 3 ada 3 elemen

# z = z.astype('float64')     # ngeubah typenya jadi float
# print(z)



# # Satu dimensi dengan satu isi
# a = np.array([1])
# print(a.ndim)
# print(a.shape)



# # Bikin array dari sebuah range angka
# print(np.arange(10))        # bikin array dari angka 0 sampe 9
# print(np.arange(1, 10))     # mulainya dari 1 sampe 10
# print(np.arange(1, 10, 2))  # isi arraynya loncat 2 angka



# # Bikin array dengan angka random (nilainya antara 0 sampe 1)
# print(np.random.random(10))
# print(np.random.rand(2, 4))                 # 2 elemen, tiap elemen berisi 4
# print(np.random.randint(7, size=10))        # munculin 10 angka random antara 1 sampe 7
# print(np.random.randint(7, size=(2, 5)))    # munculin 2 elemen masing2 berisi 5 elemen dengan angka random antara 1 sampe 7



# # Spacing
# print(np.linspace(1, 100, 5))       # nampilin angka 1 sampe 100 dicacah jadi 5 bagian



# a = [(1,2,3), (4,5,6), (7,8,9)]
# a = np.array(a)

# print(a[0:2, 0:2])
# print(a[0:, 0:2])       # semua elemen dimana masing2nya yg keluar elemen 0 sampe 1
# print(a[0:, 0:1])       # 2 Dimensi
# print(a[0:, 0])         # 1 Dimensi
# print(a[0:, [0,2]])     # yg keluar cuma elemen ke 0 sama 2 nya aja
# print(a[0:, [0,-1]])    # yg keluar cuma elemen ke 0 sama terakhir nya aja



# # Cari max, min, mean, dan median
# x = [1, 2, 3, 4, 5]
# x = np.array(x)
# print(x.max())
# print(x.min())
# print(x.sum())
# print(np.mean(y))
# print(np.median(y))

# # Cari pi, sin cos
# print(np.pi)
# print(np.sin(0))
# print(np.cos(0))



# # Reshape
# a = [(1,2,3,4,5), (4,5,6,7,8), (7,8,9,10,11)]
# a = np.array(a)

# print(a[0:, :1])    # size=3 shape=(3,1)
# print(a[0:, :1].reshape(3,))
# print(a[0:, 0])     # size=3 shape=(3,)
# print(a[0:, 0].reshape(3,1))

# print(y.reshape(-1))        # ketika gatau jumlahnya tapi pengen direshape jadi 1 dimensi
# print(y.reshape(2, -1))     # ketika gatau jumlahnya tapi pengen direshape jadi 2 dimensi dengan 2 isi -> isinya masing2 terserah
# print(y.reshape(-1, 1, 2))  # ketika gatau jumlahnya tapi pengen direshape jadi 3 dimensi dengan isi pertamanya terserah -> isi keduanya 1 -> isi ketiganya 2



# # Penjumlahan matriks
# a = [(1,2), (3,4)]
# print(a + a)    # kalo list jadi kayak dikali 2
# a = np.array(a)
# print(a + a)    # jadi operasi penjumlahan matriks

# A = np.array([
#     (0, -7),
#     (-1, 3)
#     ])

# B = np.array([
#     (2, 4),
#     (3, 8)
#     ])

# print(A + B)
# print(A - B)
# print(A + 2)    # tiap elemen dijumlah 2

# x = np.array([1, 2, 3, 4])
# x[0] += 2   # yg dijumlah 2 cuma elemen ke 0 nya aja
# print(x)



# # SPLSV
# # 3x = 6

# x = np.array([[3]])     # harus 2 dimensi
# y = np.array([6])
# z = np.linalg.solve(x, y)
# print(z)



# # SPLDV
# # 2x + y = 5
# # x + y = 7

# a = np.array([
#     (2,1),
#     (1,1)
#     ])
# b = np.array([5,7])
# hasil = np.linalg.solve(a, b)
# print(hasil)