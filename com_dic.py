d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
d3 = {}

for k in d1.keys():
    if k in d2.keys():
        d3.update({k: d1[k] + d2[k]})
    else:
        d3.update({k: d1[k]})
for key in d2.keys():
    if key not in d3.keys():
        d3.update({key: d2[key]})
print(d3)
