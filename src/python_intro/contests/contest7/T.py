l = list(map(int, input().split()))
m = dict()
for i in range(0, len(l)):
    if l[i] in m.keys():
        m[l[i]] += 1
    else:
        m[l[i]] = 1

n = []
for key, value in m.items():
    if value == 1:
        n.append(key)

for item in n:
    print(item, end=" ")

