import pandas as pd
import numpy as np

df=pd.DataFrame({'America':[21,22,23],
                 'London':[31,32,33],
                 'Dubai':[41,42,43]})

print(df)
print("Size = ",df.size)
print(df.melt())

