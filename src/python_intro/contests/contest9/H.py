N = int(input())
a = set(range(1, N + 1))

while True:
    g = input()
    if g == "HELP":
        break

    g = set(map(int, g.split()))
    yes = a & g
    if len(yes) <= len(a) // 2:
        a -= g
        print("NO")
    else:
        print("YES")
        a = yes

print(*sorted(a))