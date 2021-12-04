#Дан список размера N. Найти номера тех элементов список, которые больше своего
#левого соседа, и количество таких элементов. Найденные номера выводить в порядке
#их убывания.

from random import randint

list = []
list_sort = []

n = int(input('Введите количество элементов: '))
count = 0

while count < n:
    list.append(randint(0, 1000))
    count += 1

print(list)

for i in range(1, len(list)):
    if list[i] > list[i - 1]:
        list_sort.append(i)

print(list_sort[::-1])