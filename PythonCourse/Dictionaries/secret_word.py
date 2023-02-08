def get_dict():
    dictionary = {}
    for _ in range(int(input())):
        letter, num = input().split(': ')
        dictionary[num] = letter
    return dictionary

def get_secret_word(dictionary, code):
    code_set = set(code)
    for el in code_set:
        counter = code.count(el)
        code = code.replace(el, dictionary[str(counter)])
    return code
code = input()

dict_word = get_dict()
secret_word = get_secret_word(dict_word, code)
print(secret_word)