# def is_leap(year):
#     leap = False
    
#     # Write your logic here
#     if year%4==0:
#         return leap

# year = int(input())
# print(is_leap(year))
# year=int(input())
# leap_year=int(input())
n=int(input())
def leap_year(year):
    if n%4==0:
       print(True)
    else:
        print(False)  
        #  print(True) 

    # return(leap_year)

leap_year (n) 
# print()   

def is_leap(n):
    if year%4==0:
        print(True)
    else:
        print(False)  
        #  print(True) 

    # return(leap_year)

# leap_year (year) 
year = int(input())
is_leap(year)

def is_leap(year):
    leap = False
    
    # Write your logic here

    if year%4==0:
        leap=True
    elif year%400==0:
        leap=True 
    elif year%100==0:
        leap=True        
    # else:
    #     print(False)
    return leap

year = int(input())
print(is_leap(year))