veggies=("cucumber","tomato","potato","ladyfinger","onion")

for val in veggies:
    print(val)

#----------------- for loop in tuples ----------------     

tup=(1,2,3,4,5,6,)

for val in tup:
    print(val)

#---------------- for loop on strings ---------------

str=("Vanshika")

for char in str:
    print(char)

 #------------- else in for loop -------------------

str1 = "Vanshika"

for char in str1:
    if(char=="s"):
        print("s found")
        break
    print(char)

else:
    print("end")
