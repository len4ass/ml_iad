l = list(map(int, input().split()))
el = 1001
for i in range(0, len(l)):
    if 0 < l[i] < el:
        el = l[i]

print(el)

