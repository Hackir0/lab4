import math


class Triangle:
    def checkingForExistence(a, b, c):
        if a + b > c and a + c > b and b + c > a:
            return True
        else:
            return False

    def square(a, b, c):
        p = (a + b + b) / 3
        square = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("Площадь треугольника равна: " + str(square))

    def perimetr(a, b, c):
        perimetr = a + b + c
        print("Периметр треугольника равен:" + str(perimetr))


a = int(input("Введите сторону a = "))
b = int(input("Введите сторону b = "))
c = int(input("Введите сторону с = "))
tack = Triangle
if tack.checkingForExistence(a, b, c):
    tack.square(a, b, c)
    tack.perimetr(a, b, c)
else:
    print("Треугольника не существует ")
