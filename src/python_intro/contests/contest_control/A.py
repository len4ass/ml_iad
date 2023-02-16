a, b, c, d = int(input()), int(input()), int(input()), int(input())

price = a * 100 + b
paid_pride = c * 100 + d
change = paid_pride - price

print(change // 100, change % 100)

