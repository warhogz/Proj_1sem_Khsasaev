#Из предложенного текстового файла (text18-27.txt) вывести на экран его содержимое,
#количество пробельных символов. Сформировать новый файл, в который поместить текст
#в стихотворной форме предварительно поставив последнюю строку фразой введенной
#пользователем.

import string


text = open('text18-27.txt', encoding='utf-16').read()   # чтение текста из файла и трансляция его в консоль
print(text)

for p in string.punctuation + '\n':    # удаление пунктуации для последующего подсчета букв
    if p in text:
        text = text.replace(p, '')
count = 0
for letter in text.replace(" ", ""):   # подсчет строчных букв
    if letter.islower():
        count += 1
print('Строчных букв в исходном файле', count)

print(open('text18-27.txt', encoding='utf-16').read(172), file=open('new_file.txt', 'w', encoding='utf-8'))

with open('new_file.txt', 'a', encoding='utf-8') as f_in:
    f_in.write(input('Введите строку для записи последней строкой: '))