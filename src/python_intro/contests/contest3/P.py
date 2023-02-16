k = 0
m = 1
i = int(input())

if i == 1 or i == 2:
    print(1)
else:
    m = 0
    k = 1
    c = 2
    s = 1
    while c <= i:
        c += 1
        m, k = k, m + k

    print(k)


