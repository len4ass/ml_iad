s = input()

left = s.find("h")
right = s.rfind("h")
rotated = s[:(left + 1)] + s[(left + 1):right][::-1] + s[right:]
print(rotated)