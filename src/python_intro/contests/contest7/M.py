l = list(map(int, input().split()))
for i in range(0, len(l) // 2):
    l[i], l[len(l) - i - 1] = l[len(l) - i - 1], l[i]

for item in l:
    print(item, end=" ")

