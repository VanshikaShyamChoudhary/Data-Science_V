# Nested list challenge: Given this matrix:

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# Write code to calculate the sum of each row and print the result as a list, like [6, 15, 24].

matrix =[[1, 2, 3],[4, 5, 6],[7, 8, 9]]
ttl_matrix1=0
ttl_matrix2=0
ttl_matrix3=0

for i in range(1,4):
    ttl_matrix1+=i
# print(ttl_matrix1)

for i in range (4,7):
    ttl_matrix2+=i
# print(ttl_matrix2)

for i in range(7,10):
    ttl_matrix3+=i
# print(ttl_matrix3)

ttl_matrix=[ttl_matrix1,ttl_matrix2,ttl_matrix3]
print(ttl_matrix)

# new_matrix=((ttl_matrix+=i) for i in range matrix)



matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row_sums = []

for row in matrix:        # row = [1,2,3], then [4,5,6], then [7,8,9]
    total = 0
    for num in row:        # loop through each number in that row
        total += num
    row_sums.append(total)

print(row_sums)   # [6, 15, 24]
