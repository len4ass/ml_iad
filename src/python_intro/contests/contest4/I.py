import math

a = float(input())
b = float(input())
c = float(input())
D = b * b - 4 * a * c

if D == 0:
    x1 = (-b - math.sqrt(D)) / (a * 2)
    print(x1)
elif D > 0:
    x1 = (-b - math.sqrt(D)) / (a * 2)
    x2 = (-b + math.sqrt(D)) / (a * 2)

    if x1 > x2:
        print(x2, x1)
    else:
        print(x1, x2)