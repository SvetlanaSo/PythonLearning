with open('PythonCourse/Working with files/input.txt', encoding='utf-8') as input, \
    open('output.txt', 'w', encoding='utf-8') as output:
    for i, el in enumerate(input, start=1):
        print(f'{i}) {el}', file=output, end='')