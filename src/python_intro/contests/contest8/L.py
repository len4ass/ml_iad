t = sorted(list(map(int, input().split())))
d = sorted(list(map(int, input().split())), reverse=True)
s = 0
for k, v in zip(t, d):
    s += k * v

print(s)