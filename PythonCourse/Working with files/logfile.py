with open('PythonCourse/Working with files/logfile.txt', encoding='utf-8') as logfile, \
    open('output.txt', 'w', encoding='utf-8') as out:
    for line in logfile:
        name, start, end = line.split(', ')
        start = start[:2] + start[3:]
        end = end[:2] + end[3:]

        if int(end) - int(start) >= 100:
            out.write(name + '\n')