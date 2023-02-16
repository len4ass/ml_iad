a = int(input())
b = int(input())
c = int(input())
x = int(input())
y = int(input())
z = int(input())

d1 = (a // x) * (b // y) * (c // z)
d2 = (a // x) * (c // y) * (b // z)
d3 = (b // x) * (c // y) * (a // z)
d4 = (b // x) * (a // y) * (c // z)
d5 = (c // x) * (a // y) * (b // z)
d6 = (c // x) * (b // y) * (a // z)

if d1 >= d2:
    d2 = d1

if d3 >= d4:
    d4 = d2

if d5 >= d6:
    d6 = d5

if d4 >= d6:
    print(d4)
elif d2 >= d4 and d2 >= d6:
    print(d2)
else:
    print(d6)