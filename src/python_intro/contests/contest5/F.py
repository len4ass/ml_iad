def IsPointInSquare(x, y):
    return abs(y) <= 1 - abs(x) and abs(y) <= 1

p_x = float(input())
p_y = float(input())
print(IsPointInSquare(p_x, p_y) and "YES" or "NO")