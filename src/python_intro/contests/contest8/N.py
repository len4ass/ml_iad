def Intersection(a, b):
    new_list = []

    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else:
            new_list += [a[i]]
            i += 1
            j += 1

    return new_list

l = list(map(int, input().split()))
r = list(map(int, input().split()))
n = Intersection(l, r)
print(" ".join(list(map(str, n))))