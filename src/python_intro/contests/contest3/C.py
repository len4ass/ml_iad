i = int(input())
k = 2
while k <= i:
    if i % k == 0:
        print(k)
        break

    k += 1