import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("C:/Users/SPTINT-06/Desktop/Dataset/tips.csv")
plt.bar(data['day'],data['tip'])
plt.xlabel('day')
plt.ylabel('tip')
plt.title("bar graph")
plt.show()
data['tip'].value_counts()
print(data)
