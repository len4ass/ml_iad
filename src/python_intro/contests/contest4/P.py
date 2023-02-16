s = input()
if s.find("f") == -1:
    print(-2)
else:
    s = s.replace("f", "a", 1)
    if s.find("f") != -1:
        print(s.find("f"))
    else:
        print(-1)

