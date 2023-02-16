l = list(map(int, input().split()))
l.sort(key = lambda x: not x)
for item in l:
    print(item, end=" ")