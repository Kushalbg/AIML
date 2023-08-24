 import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("C:/Users/SPTINT-06/Desktop/Dataset/tips.csv")
plt.scatter(data['day'],data['tip'])
plt.xlabel('day')
plt.ylabel('tip')
plt.title("scatter plot")
plt.show()
data['day'].value_counts()
print(data)
