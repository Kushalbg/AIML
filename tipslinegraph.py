import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("C:/Users/SPTINT-06/Desktop/Dataset/tips.csv")
plt.plot(data['tip'])
plt.plot(data['size'])
plt.xlabel('tip')
plt.ylabel('size')
plt.title("line graph")
plt.show()
data['tip'].value_counts()
print(data)
