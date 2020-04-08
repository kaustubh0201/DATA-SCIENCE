import numpy as npy

arr1 = npy.array([[5, 6, 9], [21 ,18, 27]])
arr2 = npy.array([[15 ,33, 24], [4 ,7, 1]])

print(npy.add(arr1, arr2))
print(npy.multiply(npy.add(arr1, arr2), npy.add(arr1, arr2)))
