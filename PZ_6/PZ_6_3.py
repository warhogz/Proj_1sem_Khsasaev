# Программа выдает наибольший периметр треугольника, созданного на основе данных точек
import math
import random
X = []
Y = []
A = [X, Y]
P = []

def addpoint(x, y):
    X.append(x)
    Y.append(y)

def perimeter(x1, y1, x2, y2, x3, y3):
    a = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    b = math.sqrt(math.pow(x1 - x3, 2) + math.pow(y1 - y3, 2))
    c = math.sqrt(math.pow(x3 - x2, 2) + math.pow(y3 - y2, 2))

    p = a + b + c
    return p

n = int(input('Введите количество элементогв в списке: '))
while n:
    addpoint(random.randint(-15, 15), random.randint(-15, 15))
    n -= 1

print(A)
Max = 0

Max1 = ()
Max2 = ()
Max3 = ()

for i in range(len(A[0])):
    for e in range(len(A[0])):
        for s in range(len(A[0])):
            if A[0][i] != A[0][e] and A[0][i] != A[0][s] and A[0][e] != A[0][s] and A[1][i] != A[1][e] and A[1][i] != A[1][s] and A[1][e] != A[1][s]:
                P.append(perimeter(A[0][i], A[1][i], A[0][e], A[1][e], A[0][s], A[1][s]))
                if P[Max] < P[-1]:
                    Max = len(P)
                    Max1 = (A[0][i], A[1][i])
                    Max2 = (A[0][e], A[1][e])
                    Max3 = (A[0][s], A[1][s])

print(f'Самый большой периметр =', P[Max], 'с точками',  Max1, Max2, Max3)