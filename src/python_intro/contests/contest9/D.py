l = list(map(int, input().split()))
s = set()
for item in l:
    if item in s:
        print("YES")
    else:
        s.add(item)
        print("NO")