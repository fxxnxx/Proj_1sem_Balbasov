#Сформировать и вывести целочисленный список размера 10, содержащий степени
#двойки от первой до 10-й: 2, 4, 8,16, ... .

list = [] #пустой список для заполнения

stepen = 2
count = 0

while count < 10: #заполнение степенями 2
    list.append(stepen)
    stepen *= 2
    count += 1

print(list)