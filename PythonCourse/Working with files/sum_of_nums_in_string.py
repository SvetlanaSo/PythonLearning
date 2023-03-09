with open('PythonCourse/Working with files/numbers-2.txt', encoding='utf-8') as file:
    for line in file:
        lst = [int(line) for line in line.split()]
        print(sum(lst))
