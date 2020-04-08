import numpy as npy

arr = npy.array([[3 ,6, 9, 12], [15 ,18, 21, 24], [27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])
print(arr)

an = npy.array([], dtype = "uint32")

row, col = arr.shape

for i in range(row):
    for j in range(col):
        if i % 2 == 0 and j % 2 != 0:
            an = npy.append(an, arr[i][j])

print(an.reshape(3,2))
