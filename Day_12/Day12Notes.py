import numpy as np

# # Ngebaca file csv (angka)
# # # 1 kolom berisi masing2 id dan usia
# x = np.loadtxt('test.csv', skiprows=1, delimiter=',')
# print(x)    # jadi array

# # # 1 kolom berisi semua isi kolom id saja atau usia saja
# x = np.loadtxt('test.csv', skiprows=1, delimiter=',', unpack=True)
# print(x)

# # # Langsung dipisahkan jadi masing-masing variabel
# id, usia = np.loadtxt('test.csv', skiprows=1, delimiter=',', unpack=True)
# print(id)
# print(usia)

# # Tulis file csv
# # # Tulis ke csv lain pake numpy (usianya aja)
# np.savetxt('test2.csv', usia, fmt='%d', header='usia', comments='')

# # # Tulis ke csv lain pake numpy
# data1 = np.array(list(map(lambda a,b: [a,b], id, usia)))    # dibikin pack dulu
# np.savetxt('test3.csv', data1, fmt='%d', header='id,usia', comments='', delimiter=',')