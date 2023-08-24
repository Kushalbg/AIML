import pandas as pd
import numpy as np

dict={'first':[10,20,30,np.nan],
      'second':[np.nan,20,10,30],
      'third':[40,20,np.nan,10]}
data=pd.DataFrame(dict)
print(data)

print(data.isnull())
print(data.notnull())

print(data.fillna(0))
print(data.dropna())
print(data.fillna(method="pad"))        
print(data.fillna(method="bfill"))
print(data.replace(to_replace=np.nan,value=-59))
