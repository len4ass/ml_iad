l = list(map(int, input().split()))
tmp = l[-1]
for i in range(len(l) - 1, 0, -1):
    l[i] = l[i - 1]
l[0] = tmp

for item in l:
    print(item, end=" ")

