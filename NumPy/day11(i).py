# Program 1

# Generate

# 10 random integers
# between 50 and 100

import numpy as np
arr=np.random.randint(50,100,size=10)
print(arr)

# Program 2

# Generate

# a 4×4 matrix
# random integers
# between 1 and 20

arr1=np.random.randint(1,20,size=(4,4))
print(arr1)

# Program 3

# Generate

# 6 random decimal numbers

arr2=np.random.rand(6)
print(arr2)

# Program 4

# Randomly choose

# ["Python","Java","C++","JavaScript"]

language=["Python","Java","C++","JavaScript"]
print(np.random.choice(language))

# Program 5

# Randomly choose

# 5 colours

# from

# ["Red","Blue","Green","Black","White"]

colours=["Red","Blue","Green","Black","White"]
print(np.random.choice(colours,size=5))