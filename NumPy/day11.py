import numpy as np
# -------Random integer-----------
arr=np.random.randint(1,10)
print(arr)

#--------Random array------------
arr1=np.random.randint(1,10,size=5)
print(arr1)

#--------Random 2D array---------
arr2=np.random.randint(1,100,size=(3,4))
print(arr2)

#-------Random decimal-----------
arr3=np.random.rand(5)
print(arr3)

#--------Random 2D array---------
arr4 = np.random.rand(4,5)
print(arr4)


#--------Random choice-----------
fruits=["apple","banana","cherry","dragon fruit","emlie"]
print(np.random.choice(fruits))


#---------Random Choice Multiple Values--------
#Duplicates are possible because choices are made with replacement by default

colors=["red","blue","green"]
print(np.random.choice(colors,size=10))

# -------Seed (Very Important)-------
np.random.seed(70)

print(np.random.randint(1,100,5))