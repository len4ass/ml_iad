from itertools import accumulate
print(*list(accumulate(list(map(int, input().split())))))