import pandas as pd 
data=pd.DataFrame([[25,21,23],[29,26,28],[21,17,23]],columns=['maths','eng','kan'])
print(data)
print("\n")
print(data.sum())
print("\n")
print(data['maths'].sum())
print("\n")
print(data['eng'].min())
print("\n")
print(data['kan'].max())
print(data.value_counts())


