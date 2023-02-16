import math
cnt = 0
def sq():
    global cnt
    n = int(input())
    if n == 0:
        return

    sq()
    if int(math.sqrt(n)) ** 2 == n:
        cnt += 1
        print(n, end=" ")


sq()
if cnt == 0:
    print(0)