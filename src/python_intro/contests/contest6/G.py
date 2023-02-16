a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

m = 0
for x in range(0, 1000 + 1):
    f = a * (x ** 3) + b * (x ** 2) + c * x + d
    if f == 0 and x != e:
        m += 1

print(m)