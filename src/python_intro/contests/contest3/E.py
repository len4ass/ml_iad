def m():
    i = int(input())
    if i == 1:
        print("YES")
        return

    if i % 2 != 0:
        print("NO")
        return

    while i != 1:
        if i % 2 == 1:
            print("NO")
            return

        i //= 2

    print("YES")

m()