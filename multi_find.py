lst = [1, 2, 3, 4, 6, 7, 10]
m_lst = []

for i in range(len(lst)):
    if i == len(lst) - 1:
        break
    elif lst[i+1] - lst[i] == 1:
        continue
    else:
        k = lst[i+1] - lst[i]
        for r in range(1, k):
            m_lst.append(lst[i] + r)

print(m_lst)