''' Напишите программу, демонстрирующую работу try\except\finally'''
def sum_columns(matrix):
    result = []
    for column in zip(*matrix):
        column_sum = sum(column)
        result.append(column_sum)
    return result
import random
a = 0
while a == 0:
    try:
        m = int(input("Введите m: "))
        n = int(input("Введите n: "))
    except:
        print("Введите целое число")
    else:
        a = 1
    finally:
        print("Выполнился блок ввода размеров матрицы")
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