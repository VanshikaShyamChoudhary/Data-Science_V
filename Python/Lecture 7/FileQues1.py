# Create a new file “practice.txt” using python. Add the following data in it:

# Hi everyone.
# we are learning File I/O using Java.
# I like progranmming in Java.

# WAF that replace all occurrences of “java” with “python” in above file.
# Search if the word “learning” exists in the file or not.

with open("practice.txt","r") as f:
    data = f.read()

new_data=data.replace("Java","python")
print(new_data)    

with open("practice.txt","w") as f:
    data = f.write(new_data)