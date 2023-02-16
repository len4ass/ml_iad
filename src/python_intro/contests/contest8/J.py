n = int(input())
l = list(map(int, input().split()))
l = sorted(l)

pair_count = 0
s = 0
for i in range(0, len(l)):
    if l[i] < n:
        continue

    if l[i] == s:
        continue

    if l[i] == n:
        pair_count += 1
        s = l[i]
    elif l[i] - s >= 3:
        pair_count += 1
        s = l[i]

print(pair_count)