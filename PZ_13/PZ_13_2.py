# Составить генератор (yield), который переведет символы строки из нижнего
# регистра в верхний.

a = str(input('Введите предложение: '))

def lower_to_upper(str):
    for i in str:
        yield i.upper()

print('Итог: ', ''.join(lower_to_upper(a)))