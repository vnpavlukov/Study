import functools
import math


def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k} = {v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f'Func name is: {func.__name__}')
        print(f'vars: {signature}')
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} return {value!r}")
        func(*args, **kwargs)
        func(*args, **kwargs)
        return value

    return wrapper_debug


@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Hello, {name}!"
    else:
        return f"Oh, {name}! You are {age}, how fast you are grow"


make_greeting('Vova')
print()
make_greeting('Kate', 23)
print()

math.factorial = debug(math.factorial)


def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))


approximate_e(5)
