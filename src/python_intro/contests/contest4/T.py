s = input()
l = s.find("h")
r = s.rfind("h")
if r - l == 1:
    print(s)
else:
    f = s[(l + 1):r]
    f = f.replace("h", "H")
    print(s[:(l + 1)] + f + s[r:])