from sys import stdin

d = dict()
for line in stdin:
    if line.strip() == "":
        break

    name, pts = line.split()
    if name in d:
        d[name] += int(pts)
    else:
        d[name] = int(pts)

for key, value in sorted(d.items()):
    print(key, value)