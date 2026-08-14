# Write a recursive function to calculate the sum of first n natural numbers.
n=int(input("Enter the number : "))
sum=0
def num(n):
    if(n==0):
       return 0
    else:
      return num(n-1)+n
    
   

print(num(n))
    