# Create this matrix using reshape():
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]
import numpy as np
arr=np.array ([1 ,2 ,3 ,4,5 ,6, 7 ,8])
print(arr)
matrix=arr.reshape(4,2)
print(matrix)