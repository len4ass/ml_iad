l = list(map(int, input().split()))
for i in range(0, len(l)):
    if i % 2 == 0:
        print(l[i], end=" ")