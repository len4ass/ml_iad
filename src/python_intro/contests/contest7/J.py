l = list(map(int, input().split()))
n = int(input())
i = 0
while i < len(l) and l[i] >= n:
    i += 1
print(i + 1)

