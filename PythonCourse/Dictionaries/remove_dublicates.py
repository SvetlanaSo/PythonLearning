values = input().split()
dictionary = {}
for key in values:
    value = dictionary.get(key, 0)
    if value == 0:
        print(key, end=' ')
    else:
        print(key + '_' + str(value))
    dictionary[key] = value + 1