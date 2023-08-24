import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("C:/Users/SPTINT-06/Desktop/Dataset/tips.csv")
plt.hist(data['total_bill'])
plt.title("histogram")
plt.show()
data['tip'].value_counts()
print(data)
