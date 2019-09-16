for row in range(1, 7):
    for column in range(1, 6):
        if column == 1:
            print('*', end=' ')
        elif column == 5:
            print('*', end='\n')
        elif row == 2 and column == 2:
            print('*', end=' ')
        elif row == 2 and column == 4:
            print('*', end=' ')
        elif row == 3 and column == 3:
            print('*', end=' ')
        else:
            print(' ', end=' ')