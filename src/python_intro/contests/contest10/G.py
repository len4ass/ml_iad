from sys import stdin

d = dict()
c = 0
for line in stdin:

    if line.strip() == "":
        break

    line = line.strip("\n")
    c += 1
    if line in d:
        d[line] += 1
    else:
        d[line] = 1

l = []
for key, value in d.items():
    l += [(value, key)]

l.sort(reverse=True)
if (l[0][0] / c) > 0.5:
    print(l[0][1])
else:
    print(l[0][1])
    print(l[1][1])