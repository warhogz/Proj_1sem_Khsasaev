#Даны числа x, у. Проверить истинность высказывания: «Точка с координатами (x, у) лежит
#во второй или третьей координатной четверти».
try:
    print("Введите координаты точки x и y")
    x_point = float(input("x = "))
    y_point = float(input("y = "))

    if x_point < 0:
        print('true')
    else:
        print("false")
except ValueError: #обработка исключений
    print("Введите число!")