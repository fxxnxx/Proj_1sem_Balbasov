N = int(input('Введите целое число: '))

a = 0

while (N > 0) and (a == 0):

    if ((N % 10) % 2 != 0):

        print('True')

        a = 1

    else:

        N //= 10

if a != 1:
    print('False')