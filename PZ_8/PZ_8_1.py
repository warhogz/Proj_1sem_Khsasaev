# Организовать словарь на 10 англо-русских слов, обеспечивающий
# "перевод" английского слова на русский.
vcb = {'love': 'любовь', 'winter': 'зима', 'water': 'вода', 'help': 'помощь',
       'tree': 'дерево', 'relationships': 'отношения', 'translator': 'переводчик', 'difficult': 'сложно',
       'spring': 'весна', 'price': 'цена'}

print('Добро пожаловать!')
while True:
    try:
        search = input('Введите слово: ')
        if search == 'завершить' or search == 'quit':
            print('До свидания.')
            break
        print(search + ' - ' + vcb[search])
        print('ENG' + (' ' * (len(search))) + 'RUS')
        print()
    except KeyError:
        print('Ошибка. Слова не существует в вокабуляре программы')
        print()