a, b, c, d, e, f = float(input()), float(input()), float(input()), float(input()), float(input()), float(input())
x, y = 0, 0
determinant = a * d - b * c
determinant_x = e * d - b * f
determinant_y = a * f - e * c
x_nil = a == 0 and c == 0
y_nil = b == 0 and d == 0
if determinant != 0:
    x = determinant_x / determinant
    y = determinant_y / determinant
    print(2, x, y)
else:
    if determinant_x == 0 and determinant_y == 0:
        if x_nil and y_nil:
            if e != 0 or f != 0:
                print(0)
            else:
                print(5)
        elif x_nil:
            if b != 0:
                y = e / b
            else:
                y = f / d

            print(4, y)
        elif y_nil:
            if a != 0:
                x = e / a
            else:
                x = f / c

            print(3, x)
        else:
            k = 0
            bi = 0
            if b != 0:
                bi = e / b
                k = -a / b
            else:
                bi = f / d
                k = -c / d

            print(1, k, bi)
    else:
        print(0)