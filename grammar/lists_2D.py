matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(matrix[0][1])     # [row] [column]
matrix[0][1] = 20
print(matrix)
print(matrix[0][1])

print("")

for row in matrix:
    for item in row:
        print(item)




