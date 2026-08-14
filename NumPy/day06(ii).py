import numpy as np

a=((2,4,5),(5,6,7),(8,9,2))
b=[[0,4,5],[6,0,8],[0,5,0]]
arr=np.array(a)
arr1=np.array(b)

print(arr)
print(arr1)


print(np.sqrt(arr))


print(type(np.where(arr>8)))
print((np.where(arr>8)))


# print(np.count_nonzero(a))
# print(np.count_nonzero(b))

print(np.nonzero(a))
print(np.nonzero(b))
arr[1,2]=0
arr1[1,2]=0
print(np.nonzero(a))
print(np.nonzero(b))
