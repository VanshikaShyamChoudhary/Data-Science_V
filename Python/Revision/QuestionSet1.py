# Count vowels in a string.
str="Vanshika"
count=0

for char in str:
   if char in "aeiouAEIOU":
    count+=1
print(count)

# Swapping of numbers without 3rd variable
a=3
b=4

a=a+b
b=a-b
a=a-b
print("numbers after swaping :") 

print(a)
print(b)

# Reverse a string.

name="Vanshika"
print(name[::-1])
# 2nd method
reverse="" 
for ch in name:
  reverse = ch+reverse

print(reverse)

# Check whether a string is a palindrome.

pal=input("Enter a string : ")
reverse=""
 
for char in pal:
  reverse=char+reverse


if (reverse==pal):
    print("Palindrom")

else:
    print("Not Palindrom")  
    

# Lists-----------
# Find the largest element in a list.

list=("hagsh","hd","hsddjfeunfe","hfue")
idx=0
  
for el in list:
   print(len(list))
   idx+=1
   
# Find the sum of all list elements.
# Remove duplicates from a list.
# Tuples
# Count how many times a number appears in a tuple.
# Sets
# Find the union of two sets.
# Find the intersection of two sets.
# Dictionaries
# Create a dictionary of five students and marks.
# Print all keys.
# Print all values.
# Update one student's marks.
# Conditions
# Find the greatest of three numbers.
# Calculate grades.
# Loops
# Factorial.
# Prime number.
# Fibonacci.
# Reverse a number.
# Functions
# Write a function to find the square of a number.
# Write a function to check whether a number is even.
# Write a function to calculate the factorial.
# Recursion
# Factorial using recursion.
# Fibonacci using recursion.
# File Handling
# Create a file and write your name.
# Read the file.
# Count the number of lines in a file.
# Count the number of words in a file .