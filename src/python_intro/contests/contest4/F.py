import math
p = float(input())
a = p - math.floor(p)
print(int(p), int(round(a, 2) * 100))