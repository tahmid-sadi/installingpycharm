for r in range(6):
    for c in range(5):
        if c == 0:
            print('*', end=' ')
        elif r == 1 and (c == 1 or c == 3):
            print('*', end=' ')
        elif r == 2 and c == 2:
            print('*', end=' ')
        elif c == 4:
            print('*', end='\n')
        else:
            print(' ', end=' ')