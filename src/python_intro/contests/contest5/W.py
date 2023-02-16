def lagrange(value, power, amount):
    root = int(value ** (1 / power))
    if (value - root ** power) == 0:
        return [root ** power]

    if amount == 1:
        return []

    while len(lagrange(value - root ** power, power, amount - 1)) == 0:
        root -= 1
        if root <= 0:
            return []

    return [root ** power] + lagrange(value - root ** power, power, amount - 1)

n = int(input())
l = lagrange(n, 3, 7)
if len(l) == 0:
    print(0)
else:
    print(*l)