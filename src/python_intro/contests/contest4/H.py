n = int(input())
x = float(input())
result = 0

while n != 0:
    c = float(input())
    result += c
    result *= x
    n -= 1

c = float(input())
result += c
print(result)