import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
dummy_age_list=[12,13,15,20,25,32,30,28,35,40,42,50,55,39,60,68,64,56,22,11]
dummy_sex_list=['male','female','female','male','female','male','male','female','male','female','female','female','male','male','female','male','female','male','female','male']
df_age_sex=pd.DataFrame({'AGE':dummy_age_list,'Gender':dummy_sex_list})

print(df_age_sex)


df_age_sex.hist()
df_age_sex.plot.bar()
sns=set(style='darkgrid')
a=sns.countplot(x='Gender',data=df_age_sex)

