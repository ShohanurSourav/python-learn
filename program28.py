matrix = [
    [1, 2, 3],
    [4, 5, 6],
]
print(matrix[0][2])


# print matrix value using nested loop
matrix = [
    [1, 2, 3],
    [4, 5, 6],
]
for row in matrix:
    for col in row:
        print(col)


matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
]
# 0 row 2nd coloumn/3rd index value changed to 10
matrix1[0][2] = 10
print(matrix1[0][2])
