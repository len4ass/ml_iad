import math
def power(a, n):
    if n == 0:
        return 1

    if n == 1:
        return a

    if n == -1:
        return 1 / a


    if n > 0:
        result = a
        for i in range(2, n + 1):
            result *= a

        return result

    result = 1 / a
    for i in range(2, abs(n) + 1):
        result *= (1 / a)

    return result

v = float(input())
p = int(input())
print(power(v, p))