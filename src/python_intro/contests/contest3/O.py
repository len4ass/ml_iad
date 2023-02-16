m = 0
c = 0
while True:
    i = int(input())
    if i == 0:
        break

    if i > m:
        m = i
        c = 0

    if i == m:
        c += 1

print(c)

