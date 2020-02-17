n = int(input('Enter: '))


class Test:
    a = []

    def __init__(self, number):
        for i in range(number):
            self.a.append(i*i)

    def find_even(self):
        for i in range(n):
            if self.a[i] % 2 == 0:
                print(self.a[i])


Check = Test(n)
print(Check.a)
Check.find_even()
