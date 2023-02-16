p = int(input())
x = int(input())
y = int(input())
k = int(input())

rate = p / 100
dep = x + y / 100
while k != 0:
    dep += dep * rate
    dep = int(dep * 100) / 100
    k -= 1

print(int(dep), int(dep * 100) % 100)


