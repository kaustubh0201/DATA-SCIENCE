import numpy as npy

arr = npy.array([[34,43,73],[82,22,12],[53,94,66]])

print(arr[:, npy.argsort(arr[1])])

print(arr[npy.argsort(arr[:,1])])




