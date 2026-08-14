#convert dollar to INR
n=int(input("Enter the amount : "))
def convertor(usd_value):
    inr_value=usd_value*95
    print(usd_value,"USD VALUE =", inr_value,"INR")

convertor(n)    