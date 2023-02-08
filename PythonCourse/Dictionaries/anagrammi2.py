def get_dict(sentence):
    dict_se = {}
    for el in sentence.lower():
        if el.isalpha():
            dict_se[el] = dict_se.get(el, 0) + 1
    return dict_se

dict1, dict2 = get_dict(input()), get_dict(input())
print('YES' if dict1 == dict2 else 'NO')