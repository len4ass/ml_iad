m1 = int(input())
m2 = int(input())
if m2 > m1:
    m1, m2 = m2, m1

while True:
    i = int(input())
    if i == 0:
        break

    if i > m1:
        m1, m2 = i, m1
    elif i > m2:
        m2 = i

print(m2)


