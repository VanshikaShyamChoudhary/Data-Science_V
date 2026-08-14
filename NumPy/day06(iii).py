import numpy as np
import sys


py_ar=[0,4,44,5,6,6,8]
np_arr=np.array(py_ar)

# print(len(py_ar))
# print(sys.getsizeof(py_ar))
print(sys.getsizeof(1)*len(py_ar)) #if the array is stored in python rather 
                                   #than in numpy- it uses more value

print(np_arr.itemsize)
print(np_arr.size)
print(np_arr.itemsize * np_arr.size)     #if the array is stored in numpy it relatively takes less memory                              
