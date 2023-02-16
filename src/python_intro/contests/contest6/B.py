a = int(input())
b = int(input())

if a < b:
    for i in range(a, b + 1):
        print(i, end=" ")
else:
    i = a
    while i >= b:
        print(i, end=" ")
        i -= 1


