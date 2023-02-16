from sys import stdin
d = dict()
c = 0
for line in stdin:
    line = line.strip()
    if line == "":
        break

    line = line.split()
    name = " ".join(line[:-1])
    pts = int(line[-1])
    c += pts
    d[name] = pts

p = c / 450
l = []
for key, value in d.items():
    l += [[(value / p) - int(value/p), int(value / p), value, key]]

n = sorted(l, reverse=True)
s = 0
for item in l:
    s += item[1]

i = 0
while s < 450:
    s += 1
    n[i][1] += 1
    i += 1

for item in l:
    name = item[3]
    f = 0
    for k in n:
        if k[3] == name:
            f = k[1]
            break

    print(name, f)