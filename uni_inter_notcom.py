import pandas as pd
import numpy as np
s1=pd.Series([11,3,6,2])
s2=pd.Series([3,7,11,1])
union=pd.Series(np.union1d(s1,s2))
print("\nunion of 2 series\n",union)
intersection=pd.Series(np.intersect1d(s1,s2))
print("\nintersection of 2 series\n",intersection)
notcomm=union[~union.isin(intersection)]
print("\nnot common in both series\n",notcomm)

