n = int(input('Enter value = '))
dic = {}
for n in range(1,n + 1):
    dic.update({n: n * n})
print(dic)