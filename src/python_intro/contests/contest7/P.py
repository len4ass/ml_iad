l = list(map(int, input().split()))
maximum = -838921938928923892893
index_max = 0
minimum = 83129732183921319273917321
index_min = 0
for i in range(0, len(l)):
    if l[i] > maximum:
        maximum = l[i]
        index_max = i

    if l[i] < minimum:
        minimum = l[i]
        index_min = i

l[index_min], l[index_max] = l[index_max], l[index_min]

for item in l:
    print(item, end=" ")

