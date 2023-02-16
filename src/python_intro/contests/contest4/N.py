s = input()
if s.find("f") != -1 and s.rfind("f") != -1 and s.find("f") != s.rfind("f"):
    print(s.find("f"), s.rfind("f"))
elif s.find("f") != -1:
    print(s.find("f"))


