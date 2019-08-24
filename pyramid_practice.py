height = int(input('Enter height = '))
for r in range(1, height + 1):
    for c in range(r):
        print('*', end=' ')
    print(end='\n')
hl = height - 1
for lr in range(hl):
    count = hl
    while hl > 0:
        print('*', end=' ')
        hl -= 1
    print(end='\n')
    hl = count - 1

for row in range(1, height + 1):
    for col in range(height - row):
        print(' ', end=' ')
    print('* '*row, end='\n')





