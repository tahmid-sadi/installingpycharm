a = int(input('Enter first integer: '))
b = int(input('Enter second integer: '))

c = 1

while c < a:
    c *= b
    if c == a:
        print(True)
    elif c > a:
        print(False)
    else:
        continue




