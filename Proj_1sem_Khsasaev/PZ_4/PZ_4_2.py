

n = input('Введите целое число больше единицы: ')
while type(n) != int:
    try:
        n = int(n)
        if n < 1:
            print('Введите число больше единицы! ')
            n = input('Введите число: ')
    except ValueError:
        print('Введите целое число!')
        n = input('Введите число: ')


k = 0
s = 0
while s < n:
    s +=k
    if s < n:
        k += 1
    if s>=n:
        print('Сумма равна: {}'.format(s))
        print('Последнее число ряда: {}'.format(k))
