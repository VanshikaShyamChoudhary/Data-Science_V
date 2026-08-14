import numpy as np

arr = np.array([12, 45, 7, 23, 56, 89, 34])

# Print the mean, median, and standard deviation of the array.
print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))

# Create a new array containing only the elements greater than 30

# for el in arr:
#     if el>30:
#         new_arr=el
#         print(new_arr)
new_arr=arr[arr>30]
print(new_arr)

# Multiply every element in the array by 2 and print the result.
arr1=arr*2
print(arr1)        
   