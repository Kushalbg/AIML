import pandas as pd

df=pd.DataFrame({'Product':['Apple','Banana','Mango','Carrot','Potato'],
                 'Category':['Fruit','Fruit','Fruit','Vegetable','Vegetable'],
                 'Quantity':[10,20,30,40,50],
                 'Amount':[100,200,300,400,500]})

table=df.pivot_table(index=['Product'],values=['Amount'],aggfunc=sum)

print(df)
print(table)

