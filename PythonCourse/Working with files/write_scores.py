with open('PythonCourse/Working with files/class_scores.txt', encoding='utf-8') as old, \
    open('new_scores.txt', 'w', encoding='utf-8') as new:
    for line in old:
        line = line.split()
        line[1] = int(line[1]) + 5
        if line[1] > 100:
            line[1] = 100
        print(*line, file=new)

