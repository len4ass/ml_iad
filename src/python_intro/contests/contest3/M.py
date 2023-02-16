prev = 0
c = 0
while True:
    i = int(input())
    if i == 0:
        break

    if i > prev and prev != 0:
        c += 1
    prev = i

print(c)

