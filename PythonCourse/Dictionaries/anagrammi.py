def get_dict(word):
    dict_word = {}
    for el in word:
        dict_word[el] = dict_word.get(el, 0) + 1
    return dict_word

dict1 = get_dict(input())
dict2 = get_dict(input())
print('YES' if dict1 == dict2 else 'NO')