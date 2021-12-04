#Дан список размера N. Обнулить элементы списка расположенные между его минимальным и максимальным элементами (не включая
#максимальный и минимальный элемент)

from random import randint

list = []

n = int(input('Введите количество элементов списка: '))
count = 0

while count < n: # заполнение списка элементами
    list.append(randint(0, 1000))
    count += 1

print(list)

max = list.index(max(list)) # нахождение индексов максимума и минимума
min = list.index(min(list))


if max - min == 1 or min - max == 1:
    print('Элементы между минимальным и максимальным числом отсутствуют')
    print(list)
elif max > min:
   for i in range(min + 1, max):
       list[i] = 0
   print(list)
elif max < min:
    for i in range(max + 1, min):
        list[i] = 0
print(list)