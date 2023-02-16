import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def perimeter(a, b, c):
    return a + b + c

n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())
s_a = distance(n1, n2, n3, n4)
s_b = distance(n3, n4, n5, n6)
s_c = distance(n1, n2, n5, n6)
print(perimeter(s_a, s_b, s_c))