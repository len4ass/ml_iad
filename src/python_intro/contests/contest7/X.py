l = list(map(int, input().split()))
d = dict()
for item in l:
    if item in d.keys():
        d[item] += 1
    else:
        d[item] = 1

maximum = 0
v = 0
for key, value in d.items():
    if value > maximum:
        maximum = value
        v = key

print(v)