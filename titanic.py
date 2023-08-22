import numpy as np
import pandas as pd
data=pd.read_csv("C:/Users/SPTINT-06/Desktop/Dataset/titanic.csv",index_col="Name")
print(data)
print(data.info())
print("\n")
print(data.shape)
print(data[["Ticket","Age"]])
print("\n")
print(data.loc['Peter, Master. Michael J'])
print(data.loc[data['Age']>60])
print(data.iloc[1:10,3:5])

