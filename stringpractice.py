string = 'Hello! How are you'
print(string[0:7])
Length_string = len(string)
print(Length_string)
print(string[17])
separate_string = []
separate_string.append(string.split())
print(separate_string)
print(string.lower())
print(string.upper())
print(string.capitalize())
print(string.find('How'))
print(string[-5])
print(string[-3:-1])
print(string[::-1])


def reverse_string(item):
    return item[::-1]

reversedstring = reverse_string(string)
print(reversedstring)

string1 = 'I am fine'
print(f"{string}. {string1}")


