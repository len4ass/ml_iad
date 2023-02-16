def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)

def ReduceFraction(m, n):
    g = gcd(m, n)
    return m // g, n // g

r, p = ReduceFraction(int(input()), int(input()))
print(r, p)