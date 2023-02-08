def get_dict(phonebook_size):
    phonebook = {}
    for _ in range(phonebook_size):
        value, key = input().lower().split()
        if key in phonebook:
            phonebook[key] = phonebook[key] + ' ' + value
        else:
            phonebook[key] = value
    return phonebook

def get_number(request, dictionary):
    for _ in range(request):
        result = dictionary.get(input().lower(), 'абонент не найден')
        print(result)

phonebook_dict = get_dict(int(input()))
get_number(int(input()), phonebook_dict)