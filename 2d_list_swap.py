matrix =[
    [3, 5, 9],
    [4, 5, 7],
    [9, 1, 2],
    [7, 6, 3]
]

swap_matrix = []

for c in range(0, 3):
    for r in range(len(matrix)):
        swap_matrix.append(matrix[r][c])
print(swap_matrix)

for cl in range(12):
    if cl == 3 or cl == 7:
        print(swap_matrix[cl], ' ', end=' \n')
    else:
        print(swap_matrix[cl], ' ', end='')

