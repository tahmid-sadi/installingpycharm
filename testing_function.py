def test(serial, *args):
    for number in args:
        serial.append(number)
    return serial


a = []
formed_list = test(a, 1, 2, 3, 4, 5)

print(formed_list)
formed_list.reverse()
print('reverse_list:', formed_list)









