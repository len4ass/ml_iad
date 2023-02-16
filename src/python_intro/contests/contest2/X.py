l1, w1, h1, l2, w2, h2, lc, wc, hc = int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input())

l1max = l1
w1max = w1
if l1 < w1:
    l1max = w1
    w1max = l1

l2max = l2
w2max = w2
if l2 < w2:
    l2max = w2
    w2max = l2

lcmax = lc
wcmax = wc
if lc < wc:
    lcmax = wc
    wcmax = lc


if h1 + h2 <= hc and l1max <= lcmax and w1max <= wcmax and l2max <= lcmax and w2max <= wcmax:
    print("YES")
elif l1max <= lcmax and w1max <= wcmax and l2max <= lcmax and w2max <= wcmax and h1 <= hc and h2 <= hc:
    if l1max <= lcmax and w1max <= wcmax:
        if (l2max <= wcmax - w1max and w2max <= lcmax) \
                or (w2max <= lcmax - l1max and l2max <= wcmax) \
                or (w2max <= wcmax - w1max and l2max <= lcmax) \
                or (l2max <= lcmax - l1max and w2max <= wcmax):
            print("YES")
        elif l1max <= wcmax and w1max <= lcmax:
            if (l2max <= wcmax - l1max and w2max <= lcmax) \
                    or (w2max <= lcmax - w1max and l2max <= wcmax) \
                    or (l2max <= lcmax and w2max <= wcmax - l1max) \
                    or (l2max <= lcmax - w1max and w2max <= wcmax):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")