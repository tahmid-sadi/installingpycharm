def pyramid(height):
    for row in range(1, height + 1):
        for column in range(1, height * 2):
            if column <= (height - row):
                print(' ', end=' ')
            elif (column >= ((height * 2) - (height - row))) and (column <= ((height * 2) - 1)):
                print(' ', end=' ')
            else:
                print('*', end=' ')
        print()


Height = int(input('Enter height = '))
pyramid(Height)

