from sys import stdin

d = dict()
c = 0
for line in stdin:
    if line.strip() == "":
        break

    line = line.strip("\n")
    name, supply, amount = line.split()
    if name in d:
        if supply in d[name]:
            d[name][supply] += int(amount)
        else:
            d[name][supply] = int(amount)
    else:
        k = dict()
        k[supply] = int(amount)
        d[name] = k


for key, value in sorted(d.items()):
    print(f"{key}:")
    for k, v in sorted(value.items()):
        print(k, v)