import math

n = int(input())
h = list(map(int, input().split()))

def surface(a, b, c):
    if (a + b < c or a + c < b or b + c < a):
        return 0

    p = (a + b + c) / 2
    l = p - a
    m = p - b
    r = p - c
    under_sqrt = p * l * m * r
    if under_sqrt <= 0:
        return 0

    return math.sqrt(under_sqrt)

count = 0
for i in range(0, n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if surface(h[i], h[j], h[k]) != 0:
                count += 1

print(count)

