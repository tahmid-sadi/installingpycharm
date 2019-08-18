lst = [4, 5, 7, 8, 9, 10, 11]

c_n = lst[0]
for e in range(len(lst)):
    if c_n == lst[e]:
        c_n += 1
    else:
        print(c_n)
        break
