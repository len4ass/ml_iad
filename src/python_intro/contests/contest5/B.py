def min4(a, b, c, d):
    return min(a, min(b, min(c, d)))

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
print(min4(n1, n2, n3, n4))