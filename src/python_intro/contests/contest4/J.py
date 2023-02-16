a, b, c, d, e, f = float(input()), float(input()), float(input()), float(input()), float(input()), float(input())

determinant = a * d - b * c
x = (e * d - b * f) / determinant
y = (a * f - e * c) / determinant
print(x, y)