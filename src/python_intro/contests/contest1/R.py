rub = int(input())
kop = int(input())
i = int(input())

s = kop * i
s += rub * 100 * i

r = s // 100
k = s % 100
print(f"{r} {k}")