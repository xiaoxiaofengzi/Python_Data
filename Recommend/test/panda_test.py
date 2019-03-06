import numpy as np
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3,4,5], 'B': [4, 5, 6,7,8], 'C': [7, 8, 9,0,1]})
# print(df['A'].values)
# print(type(df['A'].values))
print(df.iloc[:,1:])