# Basic manipulation: Create a list of 10 numbers.
# Write code to print only the even numbers, and separately, the sum of all odd numbers.

my_list=[1,2,3,4,5,6,7,8,9,10]
count=0
# sum=0
for i in my_list:
    if i%2==0:
       print(i)
for i in my_list:
    if i%2!=0:
      count+=i
    #   sum=count
    #   print(count)
print("sum of all odd numbers :",count)


