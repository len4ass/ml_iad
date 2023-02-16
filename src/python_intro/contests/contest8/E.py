l = list(map(int, input().split()))
a = sorted(l)

left = a[-1] * a[0] * a[1]
right = a[-1] * a[-2] * a[-3]
if left > right:
    print(a[-1], a[0], a[1])
else:
    print(a[-3], a[-2], a[-1])