# В матрице найти минимальный и максимальный элементы.

from random import randint

strok = int(input('Введите количество строк в матрице: '))
stolb = int(input('Введите количество столбцов в матрице: '))
mat = [[randint(0, 10) for i in range(stolb)] for j in range(strok)]
print(f"Матрица: ")

for i in mat:
    print(str(i))

up = [max(i) for i in mat]
down = [min(i) for i in mat]
print(f"Максимальный элемент матрицы: {max(up)}\nМинимальный элемент матрицы: {min(down)}")