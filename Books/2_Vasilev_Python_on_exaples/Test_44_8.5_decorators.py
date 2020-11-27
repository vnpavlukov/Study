from math import exp, sin, cos, tan


def F(f):
    return lambda x: exp(-f(x) ** 2)


def Q(f):
    def q(x):
        return tan(f(x))

    return q


@F
def f(x):
    return sin(x)


@F
def g(x):
    return cos(x)


@Q
@F
def h(x):
    return x

