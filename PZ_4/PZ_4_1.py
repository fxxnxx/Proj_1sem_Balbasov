a = input('Введите A: ')
b = input('Введите B: ')
k = 0
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print('число не целое')
        a = input('Введите целое число а!!!')


while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print('число не целое')
        b = input('Введите целое число а!!!')


if a >= b:
    print('А не должно быть больше А')

while b >= a:
    b = b - 1
    k = k + 1
    print(b)

print('Колличество чисел между A и B: ', k - 1)
