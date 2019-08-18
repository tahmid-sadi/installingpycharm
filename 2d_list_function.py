matrix = [
    [4, 7, 5],
    [6, 2, 1],
    [9, 7, 8],
    [7, 3, 5]
]

f_c_x = int(input('Enter x: '))
f_c_y = int(input('Enter y: '))
s_c_x = int(input('Enter x1: '))
s_c_y = int(input('Enter y1: '))


def addition(p_list, x, y, x1, y1):
    add = p_list[x][y] + p_list[x1][y1]
    return print(add)


def multiplication(m_list, a, b, a1, b1):
    multiply = m_list[a][b] * m_list[a1][b1]
    return print(multiply)


addition(matrix, f_c_x, f_c_y, s_c_x, s_c_y)

multiplication(matrix, f_c_x, f_c_y, s_c_x, s_c_y)


