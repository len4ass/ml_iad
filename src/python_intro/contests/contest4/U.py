import math

a = float(input())
b = float(input())
c = float(input())
if a == 0:
    if b == 0 and c == 0:
        print(3)

    if b != 0 and (c != 0 or c == 0):
        x1 = -c / b
        print(1, x1)

    if b == 0 and c != 0:
        print(0)
else:
    D = b * b - 4 * a * c

    if D > 0:
        x1 = (-b - math.sqrt(D)) / (a * 2)
        x2 = (-b + math.sqrt(D)) / (a * 2)
        print(2, min(x1, x2), max(x1, x2))
    elif D == 0:
        x = -b / (a * 2)
        print(1, x)
    elif D < 0:
        print(0)