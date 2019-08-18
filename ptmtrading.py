members = ["Emran", "Sharjeel", "Shuvro", "Tahmid"]
for nm in members:
    print(nm, end = ' ')
print()
for i in range(len(members)):
    print(members[i], end = ' ')
print()
number = int(input("Enter number = "))
for i in range(1,number + 1):
    for j in range(1,i + 1):
        print(i, end = ' ')
    print('\n', end ='')

for i in range(1,number + 1):
    for j in range(1,i + 1):
        print(j, end = ' ')
    print('\n', end ='')