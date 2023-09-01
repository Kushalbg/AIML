import pandas as pd

df=pd.DataFrame({'First Name':['Aryan','Rohan','Riya','Yash','Siddhant'],
                 'Last Name':['Singh','Agarwal','Shah','Bhatiya','Khanna'],
                 'Type':['Full time Employee','Intern','Full time Employee','Part time Employee','Full time Employee'],
                 'Departement':['Administration','Technical','Administration','Technical','Management'],
                 'YOE':[2,3,5,7,6],
                 'Salary':[20000,5000,10000,10000,20000]})
                 
print(df)  

print()

table=df.pivot_table(index=['Type','Departement'],values=['Salary'],aggfunc='mean')             
print(table)

print()

table=df.pivot_table(index=['Type'],values=['Salary'],aggfunc=['sum','mean',len])             
print(table)



