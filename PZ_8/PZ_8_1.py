vcb = {'весна': 'spring', 'зима': 'winter', 'вода': 'water', 'лошадь': 'help',
       'дерево': 'tree', 'отношения': 'relationships', 'переводчик': 'translator', 'сложно': 'difficult',
       'любовь': 'love', ' цена': 'price'}

print('Добро пожаловать!')
while True:
    try:
        search = input('Введите слово: ')
        if search == 'завершить' or search == 'quit':
            print('До свидания.')
            break
        print(search + ' - ' + vcb[search])
        print('RUS' + (' ' * (len(search))) + 'ENG')
        print()
    except KeyError:
        print('Ошибка. Слова не существует в вокабуляре программы')
        print()