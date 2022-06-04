#Найти сумму отрицательных элементов первой трети матрицы.

from random import randint

strok = int(input('Введите количество строк в матрице: '))
stolb = int(input('Введите количество столбцов в матрице: '))
mat = [[randint(-10, 10) for i in range(stolb)] for j in range(strok)]
print(f"Матрица: ")

for i in mat:
    print(str(i))

s = 0

for i in range(0, round(strok/3)):
    for k in range(stolb):
        if mat[i][k] < 0:
            s += int(mat[i][k])


print('\nСумма отрицательных элементов 1й трети матрицы: =', s)