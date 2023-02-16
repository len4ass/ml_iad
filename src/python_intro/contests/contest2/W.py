def distance(l_1, r_1, l_2, r_2):
    result = max(l_1, l_2) - min(r_1, r_2)
    if result <= 0:
        return 0

    return result

l1 = int(input())
r1 = int(input())
l2 = int(input())
r2 = int(input())
l3 = int(input())
r3 = int(input())

distfs = distance(l1, r1, l2, r2)
distst = distance(l2, r2, l3, r3)
distft = distance(l1, r1, l3, r3)

count = (distfs == 0) + (distst == 0) + (distft == 0)
if count >= 2:
    print(0)
else:
    d1 = r1 - l1
    d2 = r2 - l2
    d3 = r3 - l3
    if distst <= d1:
        print(1)
    elif distft <= d2:
        print(2)
    elif distfs <= d3:
        print(3)
    else:
        print(-1)