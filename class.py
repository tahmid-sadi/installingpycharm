n = int(input('Enter: '))


class Test:
    a = []

    def __init__(self, number):
        for i in range(number):
            self.a.append(i*i)


Check = Test(n)
print(Check.a)
