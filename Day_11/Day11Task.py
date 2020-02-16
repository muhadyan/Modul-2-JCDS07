# # 1. Import numpy as np and print the version number.
import numpy as np
# print(np.__version__)

# # 2. Create a 1D array of numbers from 0 to 9
# print(np.arange(10))

# # 3. Create a 3×3 numpy array of all True’s
# print(np.full((3,3), 1, dtype=bool))

# # 4. Extract all odd numbers from arr
# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(arr[arr % 2 != 0])

# # 5. Replace all odd numbers in arr with -1
# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(np.where(arr % 2 != 0, -1, arr))

# # 6. Replace all odd numbers in arr with -1 without changing arr
# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# out = np.where(arr % 2 != 0, -1, arr)
# print(out)
# print(arr)

# # 7. Convert a 1D array to a 2D array with 2 rows
# print(np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(2,-1))

# # 8. Stack arrays a and b vertically
# a = np.arange(10).reshape(2, -1)
# b = np.repeat(1, 10).reshape(2, -1)
# print(np.vstack([a,b]))

# # 9. Stack the arrays a and b horizontally
# a = np.arange(10).reshape(2, -1)
# b = np.repeat(1, 10).reshape(2, -1)
# print(np.hstack([a,b]))

# # 10. Create the following pattern without hardcoding. Use only numpy functions and the below input array a
# a = np.array([1,2,3])
# print(np.r_[np.repeat(a, 3), np.tile(a, 3)])

# # 11. Get the common items between a and b
# a = np.array([1,2,3,2,3,4,3,4,5,6])
# b = np.array([7,2,10,2,7,4,9,4,9,8])
# print(np.intersect1d(a,b))

# # 12. From array a remove all items present in array b
# a = np.array([1,2,3,4,5])
# b = np.array([5,6,7,8,9])
# print(np.setdiff1d(a,b))

# # 13. Get the positions where elements of a and b match
# a = np.array([1,2,3,2,3,4,3,4,5,6])
# b = np.array([7,2,10,2,7,4,9,4,9,8])
# print(np.where(a == b))

# # 14. Get all items between 5 and 10 from a
# a = np.array([2, 6, 1, 9, 10, 3, 27])
# print(a[np.where((a >= 5) & (a <= 10))])