def even_range(start, end):
    current = start
    while current < end:
        yield current
        current += 2


for number in even_range(0, 10):
    print(number)

