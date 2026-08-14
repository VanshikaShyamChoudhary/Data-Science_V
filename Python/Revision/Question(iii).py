#Take the string " hello vanshika " and print it with: 
# 1) extra spaces removed, 
# 2) first letter of each word capitalised,
# 3) total character count (without spaces).

str=" hello vanshika "
print(str.strip(" "))
print(str.strip().title())
print(len(str.strip().replace(" ","")))