from decimal import Decimal


with open('PythonCourse/Working with files/goats.txt', encoding='utf-8') as colors, \
    open('answer.txt', 'w', encoding='utf-8') as answers:
    first_line = colors.readline()
    dict_colors = {}
    for key in colors:
        if key == "GOATS":
            break
        else:
            dict_colors[key] = 0
    colors.seek(len(dict_colors) + 1)
    total = 0
    for line in colors:
        dict_colors[line] += 1
        total += 1
    lst = []
    for key in dict_colors:
        if (dict_colors[key] * 100 // total) > 7:
            lst.append(key)
    print(*sorted(lst), file=answers, sep='', end='')
