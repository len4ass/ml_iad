n = int(input())
student_langs = []
for i in range(0, n):
    k = int(input())
    l = set()
    for j in range(0, k):
        l.add(input())

    student_langs += [l]


everyone = set.intersection(*student_langs)
someone = set.union(*student_langs)

print(len(everyone))
print(*sorted(everyone), sep="\n")
print(len(someone))
print(*sorted(someone), sep="\n")