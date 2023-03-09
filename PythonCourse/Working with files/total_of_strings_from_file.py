file = open('PythonCourse/Working with files/numbers.txt')
file_lines = [int(line.rstrip()) for line in file.readlines()]
print(sum(file_lines))
file.close()