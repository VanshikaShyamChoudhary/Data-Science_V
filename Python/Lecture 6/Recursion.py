# ------------Recursion for factorial---------------
n=int(input("Enter the number : "))
def fact(n):
    if(n==0 or n==1): # --| Base case for 
        return 1      # --| recursion (like a conditional statement)
    else:
        return fact(n-1)*n
    
print(fact(n))