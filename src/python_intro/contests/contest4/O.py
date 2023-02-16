s = input()
l = s.find("h")
r = s.rfind("h")
print(s[:l] + s[(r + 1):])

