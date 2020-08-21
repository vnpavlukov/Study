def make_array():
    a = []
    current_number = int(input())
    while current_number != 0:
        a.append(current_number)
        current_number = int(input())
    return a


def find_min_local_maximum(array):
    if len(array) < 5:
        return 0

    last_local_max_index = 0
    list_of_distance = list()

    for n in range(1, len(array) - 1):
        if array[n - 1] < array[n] > array[n + 1]:
            if last_local_max_index != 0:
                list_of_distance.append(n - last_local_max_index)
            last_local_max_index = n

    if len(list_of_distance) == 0:
        return 0
    else:
        return min(list_of_distance)


print(find_min_local_maximum(make_array()))
