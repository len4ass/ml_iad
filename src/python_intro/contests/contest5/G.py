def IsPointInCircle(x, y, xc, yc, r):
    return ((x - xc) ** 2 + (y - yc) ** 2) <= r ** 2

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
rad = float(input())
print(IsPointInCircle(x1, y1, x2, y2, rad) and "YES" or "NO")