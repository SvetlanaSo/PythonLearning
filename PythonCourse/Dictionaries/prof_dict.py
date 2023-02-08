def show_definition(dictionary, number):
    for _ in range(number):
        search_key = input().lower()
        value = dictionary.get(search_key, 'Не найдено')
        print(value)

amount_of_words = int(input())

prof_dict = {}
for _ in range(amount_of_words):
    key, value = input().split(': ')
    prof_dict[key.lower()] = value

show_definition(prof_dict, int(input()))