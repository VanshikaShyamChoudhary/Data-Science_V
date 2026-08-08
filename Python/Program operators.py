# OPERATORS
# ------------------Arithmetic operators----------------------
a=10
b=7

print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a%b)  # for finding the remainder
print(a**b) # a^b

# -------------------Relational / Comparison Operator ----------------
print(a==b)
print(a<=b)
print(a>=b)
print(a!=b)
print(a<b)
print(a>b)


# -------------------------Assignment operator -----------------------
a+=10
print("a:",a)
a*=5
print("a:",a)
a/=10
print("a:",a)
a**=5
print("a:",a)

# --------------------------Logical Operators--------------------------
print("Not operator:",not(a>b))

val1=True
val2= False
print("And operator :",val1 and val2)
print("Or operator :",val1 or val2)