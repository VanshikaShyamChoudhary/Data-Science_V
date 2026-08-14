# Function to return the string is even or odd
n=int(input("Enter the number : "))
 
def val_str(str):
    if(n%2==0):
        print(True)
    else:
        print("The number is : odd",str)
        print(val_str)

val_str(n)            