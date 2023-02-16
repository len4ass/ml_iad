a = int(input())
b = int(input())
c = int(input())

l = [a, b, c]
l = sorted(l)
a = l[0]
b = l[1]
c = l[2]
s = a ** 2 + b ** 2 - c ** 2

if a + b <= c :
    print("impossible")
elif s == 0:
    print("rectangular")
elif s < 0:
    print("obtuse")
elif s > 0:
    print("acute")

