N = int(input())
d = dict()
for i in range(0, N):
    key, value = input().split()
    d[key] = value

word = input()
for key, value in d.items():
    if key == word:
        print(value)
    elif value == word:
        print(key)


