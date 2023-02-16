with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

    winner_9 = -1
    winner_10 = -1
    winner_11 = -1

    for line in lines:
        s = line.split()
        c = int(s[2])
        m = int(s[3])

        if c == 9 and m > winner_9:
            winner_9 = m

        if c == 10 and m > winner_10:
            winner_10 = m

        if c == 11 and m > winner_11:
            winner_11 = m


    print(winner_9, winner_10, winner_11)

