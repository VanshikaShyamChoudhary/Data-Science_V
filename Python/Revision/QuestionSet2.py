# Lists-----------
# Find the largest element in a list.

list=["hagsh","hd","hsddjfeunfe","hfue"]
largest = list[0]
  
for el in list:
   if len(el)>len(largest):
      largest =el
print("Largest string is:",largest)

# Lists-----------
# Find the largest element in a list.
# 2nd method

list=("hagsh","hd","hsddjfeunfe","hfue")
idx=0
  
for el in list:
   print(len(el))
   idx+=1
   if len(el)>idx:
      largest=el
for el in list:
   print("largest string is :",largest)

# Find the sum of all list elements.

list=(2,4,5,6,7,8)

# Remove duplicates from a list.