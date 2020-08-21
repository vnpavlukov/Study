def factor(mode=True):
    def f(n, d):
        s = 1
        i = n
        while i > 1:
            s *= i
            i -= d
        return s

    d = 1 if mode else 2

    return lambda n: f(n, d)


print(factor(True)(5))
print(factor(False)(5))
