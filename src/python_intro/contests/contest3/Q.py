i = int(input())
s = 0
m = 1
k = 1
while m < i or k < i:
    m = m + k
    k = m + k
    s += 2

if m == i:
    s += 1

if m == i or i + m == k or i + k == m:
    print(s)
else:
    print(-1)