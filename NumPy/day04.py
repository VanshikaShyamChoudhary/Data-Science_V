# ARRAY CREATION IN NUMPY: Conversion of Array

import numpy as np
list_arr = np.array([[1,2,3],[5,6,6],[9,58,4]])

print(list_arr)
print(list_arr.dtype)
print(list_arr.size)
print(list_arr.shape)

list_arr=np.array({4,5,6})
print(list_arr)
print(list_arr.dtype)

# Zeroooo

zeros=np.zeros((5,7))
print(zeros)
print(zeros.dtype)

# Range
rng=np.arange((34))
print(rng)

# lin space
lspace = np.linspace(1,50,10)
print(lspace)