# Известно, что X кг шоколадных конфет стоит A рублей, а Y кг ирисок стоит B
# рублей. Определить, сколько стоит 1 кг шоколадных конфет, 1 кг ирисок, а также во сколько раз
# шоколадные конфеты дороже ирисок.
x = input('Вес шоколадных конфет(Введите целое число): ')
a = input("Стоимость шоколадных конфет в рублях: ")
y = input("Вес ирисок: ")
b = input("Стоимость ирисок в рублях: ")

try:  #обработка исключений
    x = int(x)
    print('Удачно')
except:
    print('Что-то пошло не так')


try:
    a = int(a)
    print('Удачно')
except:
    print('Что-то пошло не так')


try:
    y = int(y)
    print('Удачно')
except:
    print('Что-то пошло не так')


try:
    b = int(b)
    print('Удачно')
except:
    print('Что-то пошло не так')

sx = a / x
sy = b / y
print("Цена 1 кг шоколадных конфет: ", sy)
print("Шолодные конфеты дороже в ", sx / sy, "раз")