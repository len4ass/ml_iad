import math
def power(a, n):
    if n == 0:
        return 1

    if n == 1:
        return a

    if n == 2:
        return a * a

    return a * power(a, n - 1)

v = float(input())
p = int(input())
print(power(v, p))