def count(sz, done_clicks, max_clicks):
    clicks = [0] * sz
    for click in done_clicks:
        clicks[click - 1] += 1

    for i in range(sz):
        if max_clicks[i] < clicks[i]:
            print("YES")
        else:
            print("NO")

n = int(input())
m = list(map(int, input().split()))
k = int(input())
d = list(map(int, input().split()))
count(n, d, m)