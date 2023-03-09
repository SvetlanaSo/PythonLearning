orders = open('PythonCourse/Working with files/prices.txt')
total = 0
for order in orders:
    lst = order.split()
    total += int(lst[1]) * int(lst[2])
print(total)