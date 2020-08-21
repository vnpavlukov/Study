def print_text(txt="Знaчeниe аргумента по умолчанию."):
    print(txt)


print_text("Apгyмeнт указан явно.")
print_text()


def show_args(a, b="Bтopoй аргумент не указан."):
    print(a, b)


show_args("Пepвый аргумент.", "Второй аргумент.")
show_args("Пepвый аргумент.")


def my_func(x="l-й аргумент х.", y="2-й аргумент у."):
    print(x, y)


my_func()
my_func("Oдин из аргументов.")
my_func(y="Oдин из аргументов.")


def get_sum(*nums):
    s = 0
    for a in nums:
        s += a
    return s


print(get_sum(1, 2, 3, 4, 5))


def my_func(txt):
    print("Функция my_func:", txt)


new_func = my_func
new_func("вызов через· new_func. ")
