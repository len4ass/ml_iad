N = int(input())
a = set()
for i in range(1, N + 1):
    a.add(i)

while True:
    g = input()
    if g == "HELP":
        break

    s = set(map(int, g.split()))
    g = input()
    if g == "YES":
        a &= s
    else:
        a -= s

print(*sorted(a))