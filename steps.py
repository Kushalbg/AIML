import numpy as np
import pandas as pd
ds=pd.DataFrame({'days':[1,2,3,4,5,6,7,8,9,10],'steps':[4335,9552,7332,4504,5335,7552,8332,6504,8965,7689]})
ds["steps"]=ds["steps"]+1000
print(ds)
print(ds.loc[ds["steps"]>7000])

