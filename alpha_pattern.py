for r in range(6):
    for c in range(4):
        if r == 0 and (c == 1 or c == 2):
            print('*', end=' ')
        elif r == 1 and (c == 0 or c == 3):
            print('*', end=' ')
        elif r == 2 and (c == 0 or c == 3):
            print('*', end=' ')
        elif r == 3 and (c == 0 or c == 1 or c == 2 or c == 3):
            print('*', end=' ')
        elif r == 4 and (c == 0 or c == 3):
            print('*', end=' ')
        elif r == 5 and (c == 0 or c == 3):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()