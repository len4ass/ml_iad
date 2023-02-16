n, k = map(int, input().split())
s = []
for i in range(0, n):
    s += ['I']

for i in range(0, k):
    l, r = map(int, input().split())
    for j in range(l - 1, r):
        s[j] = '.'

print("".join(s))

