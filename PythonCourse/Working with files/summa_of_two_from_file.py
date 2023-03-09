file = open('PythonCourse/Working with files/nums.txt')
lines_list = [int(line) for line in file.read().split()] 
print(sum(lines_list))
file.close()