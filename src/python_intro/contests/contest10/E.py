from sys import stdin

d = dict()
for line in stdin:
    if line.strip() == "":
        break

    words = line.split()
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

m = 0
w = ""
for key, value in sorted(d.items()):
    if value > m:
        m = value
        w = key

print(w)