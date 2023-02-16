x1, y1, x2, y2 = map(int, input().split())
s1 = set()
s2 = set()

if x1 > y1:
    for i in range(y1, x1 + 1):
        s1.add(i)
else:
    for i in range(x1, y1 + 1):
        s1.add(i)

if x2 > y2:
    for i in range(y2, x2 + 1):
        s2.add(i)
else:
    for i in range(x2, y2 + 1):
        s2.add(i)

print(len(s1.intersection(s2)))

