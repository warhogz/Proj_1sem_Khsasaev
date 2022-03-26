#В матрице элементы строки N (N задать с клавиатуры) увеличить на 3

from random import randint

col, row, start, finish, need = [int(input(i)) for i in ("Кол-во столбцов = ", "Кол-во строк = ", "Числа от = ", "Числа до = ", "Необходимая строка = ")]

matrix = [[randint(start, finish) for _ in range(col)] for j in range(row)]

print('Исходная матрица: ')
for i in matrix:
    print(*i)
g = [i + 3 for i in matrix[need-1]]
matrix[need - 1] = g
print('Результат: ')
for i in matrix:
    print(*i)