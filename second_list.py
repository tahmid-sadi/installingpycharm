dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60, 7: 70}
for key, value in dic2.items():
    dic1.update({key: value})
for k, v in dic3.items():
    dic1.update({k: v})
print(dic1)