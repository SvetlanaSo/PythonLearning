def matrix_multiply(matrix1, matrix2, rows1, cols2, cols1):
    multi_m = [[0] * cols2 for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols2):
            for el in range(cols1):
                multi_m[i][j] += matrix1[i][el] * matrix2[el][j]
    return multi_m


size = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(size)]
power = int(input())

multi_m = matrix_multiply(matrix, matrix, size, size, size)

for i in range(power - 2):
    multi_m = matrix_multiply(multi_m, matrix, size, size, size)
             
for row in multi_m:
    print(*row)