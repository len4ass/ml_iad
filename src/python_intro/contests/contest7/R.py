l = list(map(int, input().split()))
m = list(map(int, input().split()))
l.insert(m[0], m[1])

for item in l:
    print(item, end=" ")

