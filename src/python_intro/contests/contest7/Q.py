l = list(map(int, input().split()))
k = int(input())
l.pop(k)

for item in l:
    print(item, end=" ")

