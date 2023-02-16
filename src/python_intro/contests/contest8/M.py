def merge(a, b):
    new_list = []

    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            new_list += [a[i]]
            i += 1
        else:
            new_list += [b[j]]
            j += 1

    while i < len(a):
        new_list += [a[i]]
        i += 1

    while j < len(b):
        new_list += [b[j]]
        j += 1

    return new_list

l = list(map(int, input().split()))
r = list(map(int, input().split()))
n = merge(l, r)
print(" ".join(list(map(str, n))))