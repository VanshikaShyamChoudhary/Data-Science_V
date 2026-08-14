# Search for a number x in this tuple using loop:

# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

num=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
x=int(input("Enter the value :"))

idx=0
for val in num:
    if(val==x):
        print("value found at index ",idx)
    idx+=1
    



