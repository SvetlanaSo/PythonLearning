def get_dict():
    dictionary = {}
    for _ in range(int(input())):
        letter, num = input().split(': ')
        dictionary[num] = letter
    return dictionary

def get_secret_word(dictionary, code):
    code_dict = {}
    for el in code:
        code_dict[el] = code_dict.get(el, 0) + 1
    for el in code_dict:
        code = code.replace(el, dictionary[str(code_dict[el])])
    return code
code = input()

dict_word = get_dict()
secret_word = get_secret_word(dict_word, code)
print(secret_word)