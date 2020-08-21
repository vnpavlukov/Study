def check_presents(first, second):
    steps = 0
    if 1 == len(set(first)) == len(set(second)):
        return steps

    length = len(first)
    steps = 0

    while min(first) != max(first) or min(second) != max(second):
        while True:
            delta = 0
            for i in range(length):
                if first[i] > min(first) and second[i] > min(second):
                    first[i] -= 1
                    second[i] -= 1
                    delta += 1
            if delta == 0:
                break
            else:
                steps += delta
        max_f_index = first.index(max(first))
        steps += max(first) - min(first)
        first[max_f_index] -= max(first) - min(first)

        max_s_index = second.index(max(second))
        steps += max(second) - min(second)
        first[max_s_index] -= max(second) - min(second)

    return steps


first = [1, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]
second = [1, 1, 1, 1, 1, 1]
print(check_presents(first, second))
