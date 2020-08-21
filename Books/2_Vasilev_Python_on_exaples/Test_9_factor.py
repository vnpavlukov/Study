def factor(mode=True):
    d = 1 if mode else 2

    def f(n, d):
        s = 1
        i = n
        while i > 1:
            s *= i
            i -= d
        return s
    return lambda n: f(n, d)


