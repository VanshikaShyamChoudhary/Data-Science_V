import numpy as np

n,m=map(int,input().split())

arr=[]

for i in range(n):
    row=list(map(int,input().split()))
    arr.append(row)
arr=np.array(arr)
print(arr.T)
print(arr.flatten())