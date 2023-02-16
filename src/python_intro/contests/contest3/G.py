def m():
    i = float(input())
    k = float(input())

    c = 1
    while i < k:
        i += 0.1 * i
        c += 1

    print(c)

m()



