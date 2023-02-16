s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
s3 = s1.intersection(s2)
for item in sorted(s3):
    print(item, end=" ")