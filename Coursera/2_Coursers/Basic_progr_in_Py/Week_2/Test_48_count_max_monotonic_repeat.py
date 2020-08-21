def make_array():
    a = []
    current_number = int(input())
    while current_number != 0:
        a.append(current_number)
        current_number = int(input())
    return a


def find_max_monotonic_repeat(array):
    max_monotonic_repeat = 1
    monotonic_repeat = 1

    if len(array) == 1:
        return max_monotonic_repeat

    n = 1
    up = True
    while n < len(array):
        if array[n] < array[n - 1]:
            if not up:
                monotonic_repeat = 1
            monotonic_repeat += 1
            if monotonic_repeat > max_monotonic_repeat:
                max_monotonic_repeat = monotonic_repeat
            up = True
            n += 1
        elif array[n] > array[n - 1]:
            if up:
                monotonic_repeat = 1
            monotonic_repeat += 1
            if monotonic_repeat > max_monotonic_repeat:
                max_monotonic_repeat = monotonic_repeat
            up = False
            n += 1
        else:
            if up:
                up = False
            else:
                up = True
            monotonic_repeat = 1
            n += 1

    return max_monotonic_repeat


print(find_max_monotonic_repeat(make_array()))
