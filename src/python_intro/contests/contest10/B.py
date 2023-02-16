d = dict()
with open("input.txt", "r") as f:
    for line in f:
        for word in line.strip().split():
            if word in d:
                print(d[word], end=" ")
                d[word] += 1
            else:
                print(0, end=" ")
                d[word] = 1
