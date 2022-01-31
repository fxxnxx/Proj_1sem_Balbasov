# Из предложенного текстового файла (text18-2.txt) вывести на экран его содержимое, количество знаков препинания.
# Сформировать новый файл, в который поместить текст в стихотворной форме выведя строки в обратном порядке.
z = 0
f1 = open('text18-2.txt', encoding='UTF-8')
print(f1.read())

for i in open('text18-2.txt', encoding='UTF-8'):
    for j in i:
        if j == ',':
            z += 1
        if j == '.':
            z += 1
        if j == '!':
            z += 1
        if j == ':':
            z += 1
        if j == '—':
            z += 1
        if j == '…':
            z += 1

print('\nКоличество знаков препинания: ', z)

# Обратный порядок строк
f1 = open('text18-2.txt', encoding='UTF-8')
N = f1.readlines()
N = N[::-1]
f1.close()

# Создание нового файла со строками в обратном порядке
f2 = open('text18-1.txt', 'w', encoding='UTF-8')
f2.writelines(N)
f2.close()