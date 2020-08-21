def factor(mode=True):
    def sf(n):
        s = 1
        i = n
        while i > 1:
            s *= i
            i -= 1
        return s

    def df(n):
        s = 1
        i = n
        while i > 1:
            s *= i
            i -= 2
        return s

    if mode:
        return sf  # он возвращает функцию без () что за волшебство?
    else:
        return df


def mnoz_na_tri(x):
    print(x * 3)


def mnoz_na_dva(x):
    print(x * 2)
    return mnoz_na_tri


mnoz_na_dva(2)(2)

# print(factor()(5))  # а тут он вызывает первую функцию без аргумента,
# # но потом подставляет ещё одну скобку! Что за разрыв шаблонов?
# print(factor(False)(5))
