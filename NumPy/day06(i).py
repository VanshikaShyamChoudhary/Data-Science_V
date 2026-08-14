import numpy as np

a=[[0,6,9],[0,504,67],[0,86,91],[0,101,182]]
b=[[2,3,4],[6,5,7],[8,5,6],[6,5,4]]

arr=np.array(a)
arr1=np.array(b)

# for printing array
print(arr)

# for printing the dimension of the array
print(arr.ndim)

# for printing the size of the array
print(arr.size)

# for printing the minimum element of the array and array1 in the axis=0 i.e. Column
print(arr.argmin(axis=0))
print(arr1.argmin(axis=0))

# for printing the maximum element of the array and array1 in the axis=0 i.e. Column
print(arr.argmax(axis=0))
print(arr1.argmax(axis=0))


# fror printing the array and array1 in the sorting manner
print(arr.argsort(axis=1))
print(arr1.argsort(axis=1))

# ---------------------------OPERATORS-------------------------------


# Multiplication
print (arr * arr1)

# Addition
print (arr + arr1)

# Subtraction
print (arr - arr1)

# Modulus
print (arr % arr1)

# Division
print (arr / arr1)

# -----------Square root---------
print(np.sqrt(arr))
print(np.sqrt(arr1))

# minimum
print(arr.min())
print(arr1.min())

# maximum
print(arr.max())
print(arr1.max())
print(arr.all(axis=0))





