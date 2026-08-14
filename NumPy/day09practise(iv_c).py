# flatten() converts a multi-dimensional array into a 1D array.
import numpy as np
arr=np.array([[1,2,3,4],
             [6,7,8,9]])
# print(arr)
new_array=arr.flatten()
print(new_array)