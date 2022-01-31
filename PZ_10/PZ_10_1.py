# Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых
# положительных и отрицательных чисел. Сформировать новый текстовый файл (.txt) следующего вида,
# предварительно выполнив требуемую обработку элементов.

n = ['13 7 -22 54 12 -3 -23 33']  # Последовательность чисел

# Формирование первого файла с числами
f1 = open('data_1.txt', 'w', encoding='UTF-8')
f1.writelines(n)
f1.close()

# Формирование второго файла с числами
f2 = open('data_2.txt', 'w', encoding='UTF-8')
f2.write('Исходные данные: ')
f2.writelines(n)
f2.close()

# Разбивание строки на элементы и преобразование их в числа
f1 = open('data_1.txt', encoding='UTF-8')
k = f1.read().split()
for i in range(len(k)):
    k[i] = int(k[i])
f1.close()

# Ищем максимальный элемент в файле data_1.txt
f1 = open('data_1.txt', encoding='UTF-8')
max = 0
p = 1
for i in range(len(k)):
    max = max if max > k[i] else k[i]
for i in range(round(len(k)/2)):
    if k[i] < 0:
        p *= k[i]
f1.close()

# Записываем записываем в файл data_2.txt количество элементов и максимальный из них
f2 = open('data_2.txt', 'a', encoding='UTF-8')
f2.write(f'\nКоличество элементов: {len(k)}\nМаксимальный элемент: {max}'
         f' \nПроизведение элементов меньших 0 в первой половине: {p}')
f2.close()