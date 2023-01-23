def matrix_multiply(matrix1, matrix2, rows1, cols2, cols1):
    multi_m = [[0] * cols2 for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols2):
            for el in range(cols1):
                multi_m[i][j] += matrix1[i][el] * matrix2[el][j]
    return multi_m



rows1, cols1 = [int(i) for i in input().split()]
matrix1 = [[int(i) for i in input().split()] for _ in range(rows1)]
input()
rows2, cols2 = [int(i) for i in input().split()]
matrix2 = [[int(i) for i in input().split()] for _ in range(rows2)]

multi_m = matrix_multiply(matrix1, matrix2, rows1, cols2, cols1)

for i in range(rows1):
    for j in range(cols2):
        print(str(multi_m[i][j]).ljust(4), end='')
    print()