n = int(input())
pairs = []
for i in range(0, n):
    inp = input().split()
    name = inp[0]
    result = int(inp[1])
    pairs += [[result, name]]

pairs.sort()
pairs.reverse()
for item in pairs:
    print(item[1])