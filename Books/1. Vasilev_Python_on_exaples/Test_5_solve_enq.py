def solve_enq(f, x0, n):
    x = x0
    for k in range(1, n + 1):
        x = f(x)
    return x


def enq_1(x):
    return (x ** 2 + 5) / 6


def enq_2(x):
    return (6 * x - 5) ** 0.5


x = solve_enq(enq_1, 0, 10)
print("l-e уравнение :  х   =", x)

x = solve_enq(enq_2, 4, 10)
print("2-e  уравнение :  х   =", x)
