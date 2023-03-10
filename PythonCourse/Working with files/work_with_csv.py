def read_csv():
    with open('PythonCourse/Working with files/data.csv', encoding='utf-8') as f:
        keys = f.readline().rstrip().split(',')
        lst = []
        for line in f:
            values = line.rstrip().split(',')
            lst.append(dict(zip(keys, values)))
    return lst
result = read_csv()
print(result)