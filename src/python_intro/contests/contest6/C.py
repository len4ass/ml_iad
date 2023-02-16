n = int(input())
l = 10 ** (n - 1)
r = 10 ** n

i = r - 1
while i >= l:
    if i % 2 == 1:
        print(i, end=" ")

    i -= 1