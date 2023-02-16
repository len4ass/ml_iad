n = int(input())
s = 0
f = 1
for i in range(1, n + 1):
    current = f * i
    s += current
    f = current

print(s)