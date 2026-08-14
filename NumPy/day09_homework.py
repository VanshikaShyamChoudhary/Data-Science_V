# Creates an array from 1 to 16.
import numpy as np
ar=np.arange(16)
print(ar)
# Reshapes it into a 4×4 matrix.
new=ar.reshape(4,4)
print(new)
trans=new.T
print(trans)
flat=trans.flatten()
print(flat)