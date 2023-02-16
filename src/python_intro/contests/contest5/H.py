def IsPointInArea(x, y):
    rr_h = y >= 2 * x + 2
    ll_h = x + y >= 0
    rr_l = y <= 2 * x + 2
    ll_l = x + y <= 0

    return (rr_h and ll_h and abs(x + 1) ** 2 + abs(y - 1) ** 2 <= 4) \
            or (rr_l and ll_l and abs(x + 1) ** 2 + abs(y - 1) ** 2 >= 4)

x1 = float(input())
y1 = float(input())
print(IsPointInArea(x1, y1) and "YES" or "NO")