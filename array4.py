import numpy as np
arr=np.array([[1,3,2],[6,4,7]])
print(arr)
print("sum of the array=",arr.sum())
print("maximum of the array=",arr.max())
print("minimum of the array=",arr.min())
print("minimum of the axis=",arr.min(axis=1))
print("maximum of the axis=",arr.max(axis=1))
print("cumulative sum=",arr.cumsum(axis=1))

