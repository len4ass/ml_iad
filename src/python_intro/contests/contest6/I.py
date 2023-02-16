for i in range(10, 99 + 1):
    l = i // 10
    r = i % 10
    p = 2 * l * r

    if i == p:
        print(i)