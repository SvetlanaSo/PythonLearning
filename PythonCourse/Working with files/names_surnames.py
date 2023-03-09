from random import choice
with open('PythonCourse/Working with files/first_names.txt', encoding='utf-8') as names, \
    open('PythonCourse/Working with files/last_names.txt', encoding='utf-8') as surnames:
    l_n, l_sn = names.read().split('\n'), surnames.read().split('\n')
    for _ in range(3):
        print(choice(l_n), choice(l_sn))