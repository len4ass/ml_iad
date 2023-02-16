n = int(input())
l = list(map(int, input().split()))
k = int(input())
min_diff = 2192812891892819291
v = 0
for i in range(0, len(l)):
    if abs(l[i] - k) < min_diff:
        min_diff = abs(l[i] - k)
        v = l[i]

print(v)