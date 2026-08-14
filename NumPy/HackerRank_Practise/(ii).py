import numpy as np

n,m = map(int,input().split())

arr=[]
for i in range(n):
    row=list(map(int,input().split()))
    arr.append(row) 
    
arr=np.array(arr)

sum=arr.sum(axis=0)
# print(sum)
# axis=sum
for i in sum :
    prod=sum.prod()
# prod=arr.prod(axis=0)
# print(sum)
print(prod)
    
