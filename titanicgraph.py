import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("C:/Users/SPTINT-06/Desktop/Dataset/titanic.csv")
df=pd.DataFrame(data)

print(df)
print(df.head(10))

plt.hist(df['Age'])
plt.show()

print(df['Sex'].value_counts().plot(kind='bar'))

print(df[['Sex','Pclass','Survived']])
c=df[df['Pclass']==3]
f=c[c['Sex']=='female']
c['Survived'].value_counts().plot(kind='bar')
print(f['Survived'].value_counts())

plt.scatter(data['Age'],data['Fare'])
plt.show()


