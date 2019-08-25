dic = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
dic1 = {'e': 30, 'f': 25, 'g': 60}

for v in dic.values():
    print(v, end=' ')

print()

for k in dic.keys():
    print(k, end=' ')

print()

for i in dic1.items():
    print(i, end=' ')

print()
list = []

for vl in dic.values():
    for va in dic1.values():
        list.append(vl + va)

print(list)
