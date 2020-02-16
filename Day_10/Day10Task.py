import numpy as np
# 4x + 7y = 2
# 3x + 2y = -5
# Nilai 2x - 3y ?

a = np.array([(4,7), (3,2)])
b = np.array([2,-5])
x = np.linalg.solve(a, b)
x[0] *= 2
x[1] *= 3
hasil = x[0] - x[1]
print(f'Nilai dari 2x - 3y = {int(hasil)}')



# Jumlah ayam dan kambing = 25
# Jumlah kaki = 70
# berapa banyak ayam dan kambing masing-masing

# x + y = 25
# 2x + 4y = 70

a = np.array([(1,1), (2,4)])
b = np.array([25,70])
x = np.linalg.solve(a, b)
print(f'Jumlah ayam sebanyak {int(x[0])} ekor dan jumlah kambing sebanyak {int(x[1])} ekor')



# Ali beli 2 buku, 1 pensil, 1 penghapus = 4.700
# Badar beli 1 buku, 2 pensil, 1 penghapus = 4.300
# Carli beli 3 buku, 2 pensil, 1 penghapus = 7.100
# Berapa harga buku, pensil, dan penghapus ?

# 2x + y + z = 4700
# x + 2y + z = 4300
# 3x + 2y + z = 7100

a = np.array([(2,1,1), (1,2,1), (3,2,1)])
b = np.array([4700, 4300, 7100])
x = np.linalg.solve(a, b)
print(f'Harga buku tulis Rp {int(x[0])}, pensil Rp {int(round(x[1]))}, dan penghapus Rp {int(x[2])}')



# Bikin function maks dan mins buat array
from functools import reduce
x = [1,5,2,3,4]
xsum = reduce(lambda a,b: a+b, x)
xmax = reduce(lambda a,b: a if (a>b) else b, x)
xmin = reduce(lambda a,b: a if (a<b) else b, x)