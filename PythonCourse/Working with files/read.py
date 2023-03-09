from random import choice
file = open('PythonCourse/Working with files/lines.txt', 'r')
list_of_lines = file.readlines()
print(choice(list_of_lines))
file.close()