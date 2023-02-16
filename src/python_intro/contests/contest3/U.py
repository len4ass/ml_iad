i = int(input())
m = 1
k = 0

while i != 0:
    v = int(input())
    i, v = v, i

    if v == i:
        m += 1

    if m > k:
        k = m

    if v != i:
        m = 1

print(k)