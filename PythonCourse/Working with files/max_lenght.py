with open('PythonCourse/Working with files/lines-2.txt', encoding='utf-8') as file:
    lst = [line.strip() for line in file.readlines()]
    max_lenght = len(max(lst, key=len))
    for el in lst:
        if len(el) == max_lenght:
            print(el)