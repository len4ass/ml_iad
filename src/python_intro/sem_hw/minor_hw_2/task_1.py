def morecommon(a, b, n):
    counter_a = 0
    counter_b = 0

    for item in a:
        if item % n == 0:
            counter_a += 1

    for item in b:
        if item % n == 0:
            counter_b += 1

    return counter_a > counter_b

if __name__ == '__main__':
    pass