x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())


def coord(x, y):
    if x >= 0 and y >= 0:
        return 1

    if x < 0 and y >= 0:
        return 2

    if x < 0 and y < 0:
        return 3

    if x >= 0 and y < 0:
        return 4


print(coord(x1, y1) == coord(x2, y2) and "YES" or "NO")