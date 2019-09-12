x = int(input('Enter height = '))
for i in range(1, x + 1):
    print('*' * i)
h = x - 1
while h > 0:
    print('*' * h)
    h -= 1

for j in range(1, x + 1):
    for k in range(1, j+1):
        print('*', end=' ')
    print(end='\n')

for r in range(1, x + 1):
    for c in range(1, x + 1):
        if c <= (x - r):
            print(' ', end=' ')
        else:
            print('*', end=' ')
    print()







