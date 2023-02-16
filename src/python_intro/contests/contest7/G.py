l = list(map(int, input().split()))
el = -12982189128819212891892198
index = 0
for i in range(0, len(l)):
    if l[i] > el:
        el = l[i]
        index = i

print(el, index)

