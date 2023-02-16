N, K = map(int, input().split())
days = set()
for i in range(0, K):
    b, s = map(int, input().split())
    l = set()
    for j in range(b, N + 1, s):
        if j % 7 != 6 and j % 7 != 0:
            l.add(j)
    days |= l

print(len(days))