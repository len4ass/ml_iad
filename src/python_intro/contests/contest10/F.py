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

s = []
for key, value in d.items():
    s += [(value, key)]

def sorter(lws):
    return -lws[0], lws[1]

s.sort(key = sorter)
for item in s:
    print(item[1])