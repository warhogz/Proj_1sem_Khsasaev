#В матрице найти среднее арифметическое положительных элементов, кратных 3

from random import randint

#col, row, start, finish = [int(input(i)) for i in ("Кол-во столбцов = ", "Кол-во строк = ", "Числа от = ", "Числа до = ")]
col, row, start, finish = 5, 2, -27, 27
matrix = [[randint(start, finish) for _ in range(col)] for j in range(row)]

print('Исходная матрица: ')
for i in matrix:
    print(*i)
xd = [[i for i in j if i%3==0 and i>=0] for j in matrix]
new = []
for i in xd:
    new.extend(i)
print(f'Положительные элементы матрицы, кратные трём: {new}')
print('Их среднее арифметическое значение:', sum(new)/len(new))
