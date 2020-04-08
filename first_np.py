import numpy as npy

a = npy.arange(0,8, dtype = "uint16")

m = npy.reshape(a, (4,2))

print("This is the dimensions of the array: ", m.shape)
print("The length of each element of the array in byte is: ", m.itemsize)
print("The dimension of the array is:", m.ndim)
