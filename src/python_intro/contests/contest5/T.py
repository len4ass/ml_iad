def rev():
    v = int(input())
    if v != 0:
        rev()

    print(v)


rev()