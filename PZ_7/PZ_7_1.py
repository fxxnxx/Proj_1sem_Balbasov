#Дано целое число N (32 < N < 126). Вывести символ с кодом, равным N.

import random
N = random.randrange(32, 126)
print("N = ",N,"; Номер символа: ",chr(N))