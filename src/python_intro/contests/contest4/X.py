s = input()
for i in range(0, len(s)):
    if i % 3 == 0:
        continue

    print(s[i], end = "")

