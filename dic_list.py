list = [
    [{3: 9}, {5: 25}, {1: 1}],
    [{9: 81}, {7: 49}, {2: 4}],
    [{4: 16}, {8: 64}, {3: 9}],
    [{6: 36}, {3: 9}, {2: 4}]
]

val_list = []

for r in range(len(list)):
    for c in range(len(list[r])):
        for v in list[r][c].values():
            val_list.append(v)
print(val_list)

for e in range(12):
    if e == 2 or e == 5 or e == 8:
        print(val_list[e], end=' \n')
    else:
        print(val_list[e], end=' ')