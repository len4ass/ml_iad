N, M = map(int, input().split())
a = set()
for i in range(0, N):
    a.add(int(input()))

b = set()
for i in range(0, M):
    b.add(int(input()))

print(len(a.intersection(b)))
print(*sorted(a.intersection(b)))
print(len(a.difference(b)))
print(*sorted(a.difference(b)))
print(len(b.difference(a)))
print(*sorted(b.difference(a)))