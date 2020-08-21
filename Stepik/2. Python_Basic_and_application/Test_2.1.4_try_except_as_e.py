def f(x, y):
    try:
        print(x / y)
    except (TypeError, ZeroDivisionError) as e:
        print(type(e))
        print(e)
        print(e.args)


f(4, 2)
f(5, 0)
f(5, [])
