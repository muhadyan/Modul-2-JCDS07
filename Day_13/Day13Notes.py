# PANDAS
# jika di numpy yg harus dipahami adalah = array, dimensi, shape
# jika di pandas yg harus dipahami adalah = dataframe

# py -m pip install pandas  ==> cara install pandas

import pandas as pd
import numpy as np

# Series adalah table dengan 1 kolom
# x = np.array([1,2,3,4,5,6,7,8,9])
# xSeries = pd.Series(x)
# print(xSeries)

# xDataFrame = pd.DataFrame(x)
# print(xDataFrame)

xDataFrame = pd.DataFrame([[1,2], [3,4], [4,5]], columns=['A', 'B'])
print(xDataFrame)