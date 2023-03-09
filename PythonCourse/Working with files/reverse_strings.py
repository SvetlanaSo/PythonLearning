with open('PythonCourse/Working with files/data.txt', encoding='utf-8') as file:
    lst = [line.strip() for line in file.readlines()]
    lst.reverse()
    print(*lst, sep='\n')