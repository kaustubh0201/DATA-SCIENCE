import numpy as npy

arr = npy.arange(100,200,10, dtype = "uint32")

m = npy.reshape(arr, (5,2))
print(m)
