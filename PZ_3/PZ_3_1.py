
a = input('Введите целое число а')
while type(a) != int: #обработка исключений
    try:
        a = int(a)
    except ValueError:
        a = input('Введите целое число а!!!')
if a > 0:
    print('Число положительное.')
else:
    print('Число отрицательное.')