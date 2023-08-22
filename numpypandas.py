import numpy as np
import pandas as pd

a=np.array([11,21,45,32,16])
s=pd.Series(a)
print(a)
print(s)

s=pd.Series(5,index=[1,2,3,4])
print(s)

i=pd.Index([2,1,1,np.nan,3])
print(i.value_counts())

