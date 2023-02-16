d = 0
cd = 0
md = 0
prev = int(input())
cur = 0
next_ = 0
if prev != 0:
    cur = int(input())
    if cur != 0:
        next_ = int(input())
        pos = 2
        while next_ != 0:
            if prev < cur and cur > next_:
                if d != 0:
                    cd = pos - d
                    if md == 0:
                        md = cd
                    else:
                        md = min(cd, md)

                d = pos

            pos += 1
            prev = cur
            cur = next_
            next_ = int(input())


print(md)