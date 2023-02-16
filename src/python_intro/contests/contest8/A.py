l = list(map(int, input().split()))
f = True
for i in range(1, len(l)):
    if l[i] <= l[i - 1]:
        f = False
        break

print(f and "YES" or "NO")