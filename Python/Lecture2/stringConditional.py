# ------------------------------CONDITIONNAL STATEMENTS--------------------------------------------
# age=int(input("Enter the age :"))

# if(age<18):
#  print("Person is not eligible to vote")

# else:
#  print("Person is eligilble to vote.")

#  ---------------------------------------Q--U--E--S--T--I--O--N------------------------------------------

# Grade students based on marks
# marks >= 90, grade =“A”
# 90 > marks >= 80, grade =“B”
# 80 > marks >= 70, grade =“C”
# 70 > marks, grade = “D”

marks= int(input("Enter the marks :"))

if (marks >= 90):
 grade= "A"

elif(90>marks>=80):
 grade = "B"

elif(80 > marks >= 70):
 grade ="C"

elif(70 > marks):
 grade = "D"

else:
 "Try again"

 print("Grade of the student:", grade)


