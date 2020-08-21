def parent(num):
    def f_child():
        print('First child')

    def s_child():
        print('Second child')

    if num == 1:
        return f_child
    else:
        return s_child


first = parent(1)
second = parent(2)

first()
second()
