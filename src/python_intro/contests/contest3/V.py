f = int(input())
s = int(input())
m = 1
l = 1

while True:
    if s == 0 or f == 0:
        break

    while f < s:
        l += 1
        if l > m:
            m = l
            f = s
            s = int(input())
        else:
            f = s
            s = int(input())

    l = 1
    while f > s:
        if s == 0:
            break

        l += 1
        if l > m:
            m = l
            f = s
            s = int(input())
        else:
            f = s
            s = int(input())

    l = 1
    while f == s:
        l = 1
        f = s
        s = int(input())

print(m)