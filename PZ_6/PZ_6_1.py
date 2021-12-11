# Дан список A размера N. Найти минимальный элемент из его элементов с четными
# номерами: A2, A4, A6, ... .
import random
a = []
n = int(input('Введите количество элементов в списке: '))

while n:
    a.append(random.randint(0, 100))
    n -= 1
print(a)
b = []
for i in range(len(a)):
    if (i + 1) % 2 == 0:
       b.append(a[i])
b.sort(reverse = True)

Min = b[-1]
index = int
for i in range(len(a)):
    if a[i] == Min:
        index = i

print('Минимальное значение у элемента №', index + 1, '=', Min)