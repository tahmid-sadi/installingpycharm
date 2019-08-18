def pyramid_pattern(n):
    for r in range(1, n + 1):
        for j in range(1, r + 1):
            print('*', end=' ')
        print()
    d_num = n - 1
    while d_num > 0:
        for r in range(1, d_num + 1):
            print('*', end=' ')
        print()
        d_num -= 1


Num = int(input('Enter num = '))
pyramid_pattern(Num)
