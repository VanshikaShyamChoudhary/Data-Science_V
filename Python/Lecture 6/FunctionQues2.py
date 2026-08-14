# WAF to print the elements of a list in a single line. ( list is the parameter)
num=[1,2,3,4]
hero=["balveer","shaktiman"]


def el_list(list):
    for val in list:
        print(val,end=" ")
    

el_list(num)
print()