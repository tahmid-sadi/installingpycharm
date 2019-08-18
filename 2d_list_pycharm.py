matrix = [
    [3, 6, 4],
    [9, 8, 1],
    [2, 5, 7]
]

dup_matrix = []
for r in range(len(matrix)):
    for l in range(len(matrix[r])):
        dup_matrix.append(matrix[r][l])
print(dup_matrix)

matrix_sum = 0
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        matrix_sum += matrix[r][c]
print(matrix_sum)

sum_particular_column = 0
Column = int(input("Enter column = "))
for row in range(len(matrix)):
    sum_particular_column += matrix[row][Column]
print(sum_particular_column)

sum_particular_row = 0
Row = int(input("Enter Row = "))
for column in range(len(matrix[Row])):
    sum_particular_row += matrix[Row][column]
print(sum_particular_row)
