# Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Элементы первого и второго файлов:
# Элементы первого файла, присутствующие во втором:
# Элементы второго файла, присутствующие в первом:
# Количество элементов:
# Количество отрицательных элементов:
# Количество положительных элементов:

a = '23 -45 54 2 -5 6 44 -12 34'
b = '54 -32 43 23 -43 12 -54 5'

def lenMyList(a, b):
    c = a + b
    return len(c)

def doublecheck(a, b):
    double = []
    for i1 in a:
        for i2 in b:
            if i1 == i2 and i1 not in double:
                double.append(i1)

    return double

def negposNumbers(a, b):
    pos = 0
    neg = 0

    c = a + b
    for i in c:
        if int(i) > 0:
            pos += 1

    for i in c:
        if int(i) < 0:
            neg += 1

    return pos, neg

# задание1
f1 = open('source.txt', 'w', encoding='utf-8')
f1.write('Исходные данные первого файла: ')
f1.writelines(a)
f1.write('\n')
f1.writelines(b)
f1.write('\n')
f1.close()

f2 = open('file1.txt', 'w', encoding='utf-8')
f2.writelines(a)
f2.write('\n')
f2.close()

f3 = open('file2.txt', 'w', encoding='utf-8')
f3.writelines(b)
f3.write('\n')
f3.close()

#задание2
f2 = open('file1.txt', 'r', encoding='utf-8')
a = f2.read().split()

f3 = open('file2.txt', 'r', encoding='utf-8')
b = f3.read().split()

f1 = open('source.txt', 'a', encoding='utf-8')
f1.writelines('Общие элементы файлов: ')
f1.write(str(doublecheck(a, b)))
f1.write('\n')

f1.writelines('Количество элементов: {}'.format(lenMyList(a, b)))
f1.write('\n')

f1.writelines('Количество позитивных и негативных: {}'.format(negposNumbers(a, b)))
f1.write('\n')

f1.close()