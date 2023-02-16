def fixedfloat(n):
    def decorator(fn):
        def decorated2(*x, **x_):
            y = []
            for i in x:
                if type(i) == float:
                    y += [round(i, n)]
                else:
                    y += [i]

            d = dict()
            for k, v in x_.items():
                if type(v) == float:
                    d[k] = round(v, n)
                else:
                    d[k] = v

            return fn(*y, **d)
        return decorated2
    return decorator

@fixedfloat(4)
def aver(*args, sign=1):
    return sum(args) * sign

print(aver(2.45675901, 3.22656321, 3.432654345, 4.075463224, sign=-1))