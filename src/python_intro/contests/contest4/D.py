p = int(input())
x = int(input())
y = int(input())
money = 100 * x + y
new = int(money * (p + 100) / 100)
print(new // 100, new % 100)


