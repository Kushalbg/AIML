import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("C:/Users/SPTINT-06/Documents/mtcars.csv")
print(data)
plt.hist(data['mpg'])
plt.show()

plt.scatter(data['wt'],data['mpg'])
plt.xlabel('weight')
plt.ylabel('mpg')
plt.title('scatter plot')
plt.show()
