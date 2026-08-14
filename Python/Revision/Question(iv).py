# You have a string "Vanshika,20,Delhi,DataScience". 
# Split it by comma and print each part on a new line with its position number.

str="Vanshika 20 DataScience"
parts = str.split( ",")
for i, parts in enumerate(parts):
    print(f"{i+1}.{parts}")