#Дано целое число N (>0). Найти сумму 1 + 1/2 + 1/3 + ... + 1/N

val = input("Введите целое число: ")
while type(val) != int: #обработчик условий
    try:
         val = int(val)
         if val < 0:
             print('Введите положительное число! ')
             val = input('Введите число: ')
    except ValueError:
        print('Введите число!')
        val = input('Введите число: ')

i = 1
n = 1
s = 0
while i != val + 1:
    s += 1/i
    i += 1
print(s)