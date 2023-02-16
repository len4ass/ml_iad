l = list(map(int, input().split()))
index = 0
maximum = -1821782182712
for i in range(0, len(l)):
    if l[i] >= maximum:
        maximum = l[i]
        index = i

print(maximum, index)