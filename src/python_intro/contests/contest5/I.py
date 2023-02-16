import math

n = int(input())

found_div = False
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        found_div = True
        print(i)
        break

if not found_div:
    print(n)