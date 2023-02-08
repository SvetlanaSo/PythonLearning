def get_dict(word):
    dict_word = {}
    for el in word:
        value = dict_word.get(el, 0)
        if value != 0:
            dict_word[el + str(value)] = 0
        dict_word[el] = value + 1
    return dict_word

dict1 = get_dict(input())
dict2 = get_dict(input())
print('YES' if dict1 == dict2 else 'NO')