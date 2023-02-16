def CountSort(a):
    l = []
    for i in range(101):
        l += [0]

    for i in a:
        l[i] += 1

    j = 0
    for i in range(0, 101):
        if l[i] > 0:
            for k in range(0, l[i]):
                a[j] = i
                j += 1

    return a

n = list(map(int, input().split()))
m = CountSort(n)
for item in m:
    print(item, end=" ")