def xor(x, y):
    return x ^ y

n = int(input())
n2 = int(input())
print(xor(n, n2) and "1" or "0")