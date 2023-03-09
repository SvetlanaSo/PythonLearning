with open('PythonCourse/Working with files/population.txt', encoding='utf-8') as f:
    for line in f:
        c, p = line.split('\t')
        if c.startswith('G'):
            if int(p) > 500_000:
                print(c)