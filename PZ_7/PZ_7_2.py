#Ввод текста и создание переменных

text = input('Введите текст: ')
textLen = len(text)
num = 0

# Проверка на количество символов
if textLen > 0:
    # Цикл на текст
    for i in range(1, textLen):
        # Проверка на пробелы
        if (text[i]) == ' ' and text[i - 1] != ' ':
            num += 1

    print(num + 1)
else:
    print('Вы не ввели текст!')