import math
def IsPrime(v):
    for i in range(2, int(math.sqrt(v)) + 1):
        if v % i == 0:
            return False

    return True

n = int(input())
print(IsPrime(n) and "YES" or "NO")