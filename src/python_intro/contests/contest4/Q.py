s = input()
l = s.find("h")
r = s.rfind("h")
if r - l == 1:
    print(s)
else:
    f = s[(l + 1):r]
    print(s[:(l + 1)] + f * 2 + s[r:])

