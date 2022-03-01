# В последовательности их N чисел (N –четное) в первой ее половине найти
# произведение элементов меньших 0.

n = 10
nT = []

i = -10

val = lambda val: val != 0 and val % 2 == 0
while i <= n:
    if val(i):
        nT.append(i)
    i += 1

curLen = len(nT) * 0.5

res = 1
for k, v in enumerate(nT):
    if k < curLen:
        res *= nT[v]

print('Итог:', res)