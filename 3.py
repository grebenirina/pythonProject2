' ' 'Найти сумму каждого столбца матрицы размером m*n. ' ' '
def sum_columns(matrix):
    result = []
    for column in zip(*matrix):
        column_sum = sum(column)
        result.append(column_sum)
    return result
import random
m = int(input("Введите m: "))
n = int(input("Введите n: "))
matrix = []
for i in range(m):
    row = []
    for j in range(n):
        value = random.randint(0, 10)
        row.append(value)
    matrix.append(row)
for row in matrix:
    print(row)
column_sums = sum_columns(matrix)
print("Суммы столбцов: ", column_sums)



