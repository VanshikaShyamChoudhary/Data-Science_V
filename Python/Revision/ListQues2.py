# List comprehension: Given words = ["data", "science", "python", "AI"],
# use list comprehension to create a new list containing the length of each word.

my_list=["data", "science", "python", "AI"]


new_list=[len(i) for i in my_list]
print(new_list)
    # print(len(my_list))
# my_list=[len(my_list) for i in range(1,4)]