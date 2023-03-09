with open('PythonCourse/Working with files/nums-2.txt', encoding='utf-8') as f:
    total = 0
    for line in f:
        num = ''
        for symbol in line:
            if symbol.isdigit():
                num += symbol
            else:
                if num != '':
                    total += int(num)
                    num = ''
print(total)