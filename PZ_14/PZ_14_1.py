# Из текстового файла (writer.txt) выбрать фамилии писателей, посчитать количество фамилий. Создать новый файл, в котором выполнить замену слова "роман"
# на слово "произведение".

import re

fbi = re.compile(r'[А-ЯЁ][а-яё]+ [А-ЯЁ][,.][А-ЯЁ][,. ]|[А-ЯЁ][а-яё]+-[А-ЯЁ][а-яё]+ [А-ЯЁ][,.][А-ЯЁ][,. ]')
with open('writer.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    surname = re.findall(fbi, text)
    print(f'{surname}\nКоличество фамилий: {len(surname)}')

hello = re.compile(r'\b[Рр]оман\b')

with open('roman.txt', 'w', encoding='utf-8') as roman:
    roman.write(re.sub(hello, '________ПРОИЗВЕДЕНИЕ________', text))
    print(re.sub(hello, '________ПРОИЗВЕДЕНИЕ________', text))
    print(f"Количество замен слова <роман>: {list(re.subn(hello, '________ПРОИЗВЕДЕНИЕ________', text))[-1]}")