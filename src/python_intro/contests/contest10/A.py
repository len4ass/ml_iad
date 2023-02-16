N = int(input())
d = dict()
for i in range(0, N):
    s = input().split()
    for j in range(1, len(s)):
        d[s[j]] = s[0]

K = int(input())
for i in range(0, K):
    print(d[input()])