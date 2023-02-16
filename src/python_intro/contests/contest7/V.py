l = []
for i in range(0, 8):
    x, y = map(int, input().split())
    l.append(x)
    l.append(y)

pair = False
for i in range(0, len(l), 2):
    if pair:
        break

    for j in range(i + 2, len(l), 2):
        if pair:
            break

        if l[i] == l[j] or l[i + 1] == l[j + 1] or abs(l[i] - l[j]) == abs(l[i + 1] - l[j + 1]):
            pair = True

print(pair and "YES" or "NO")