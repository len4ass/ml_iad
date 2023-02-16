def fn(l, *funcs):
    f = funcs[0]
    maximum = 0
    for func in funcs:
        s = 0
        for v in l:
            s += func(v)

        if s >= maximum:
            f = func

    return f


if __name__ == '__main__':
    pass