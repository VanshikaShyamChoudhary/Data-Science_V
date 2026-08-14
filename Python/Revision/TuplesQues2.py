# Tuple in a function:
# Write a function min_max(numbers) that takes a list of numbers and returns a tuple (minimum, maximum).
# Call it and unpack the result into two variables.
tuples = (23,84,93,3,4,95,105)
def min_max(number):
    minimum=number[0]
    maximum=number[0]

    for num in number:
        if num<minimum:
            minimum=num
        if num>maximum:
            maximum=num

    return (minimum,maximum)  
           
low, high = min_max(tuples)
print(f"Minimum: {low}, Maximum: {high}")
