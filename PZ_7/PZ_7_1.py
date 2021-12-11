# Дан символ C и строка S. Удвоить каждое вхождение символ C в строку S.
print('Добро пожаловать!')
C = input('Введите удваиваемый символ: ')
text = list(input('Введите текст: '))
textLen = len(text)

# Функция конвертации текста из списка в строку
def convert(s):
    str1 = ""
    return (str1.join(s))

# Цикл на список, с последующей добавкой символа С
for i in range(0, textLen):
    if (text[i]) == C:
        text[i] = text[i] + C

print('итоговый текст:  ' + convert(text))