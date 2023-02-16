def bin_search(val):
    if val < s[0][1]:
        return s[0][0]

    if val > s[-1][1]:
        return s[-1][0]

    left = 0
    right = len(s) - 1
    while right - left > 1:
        mid = (right + left) >> 1
        if s[mid][1] < val:
            left = mid
        else:
            right = mid

    if val - s[left][1] < s[right][1] - val:
        return s[left][0]
    else:
        return s[right][0]

n = int(input())
l = [int(item) for item in input().split()]
m = int(input())
s = [int(item) for item in input().split()]

for i in range(0, len(s)):
    s[i] = [i + 1, s[i]]

s.sort(key=lambda x: x[1])
print(*[bin_search(item) for item in l])