l = list(map(int, input().split()))
el = 10019812732193789123892137821738192372813892173817829
for i in range(0, len(l)):
    if abs(l[i]) % 2 == 1 and l[i] < el:
        el = l[i]

print(el)

