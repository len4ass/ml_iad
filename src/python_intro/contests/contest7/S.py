l = list(map(int, input().split()))
c = 0
for i in range(0, len(l)):
    for j in range(i + 1, len(l)):
        if l[i] == l[j]:
            c += 1

print(c)

