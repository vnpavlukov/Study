text = open("in.txt", 'r')
data = text.read().replace('\n', ' ').lower().split()
text.close()

data.sort()


def count_repetition(string):
    new_dict = {}
    for i in string:
        new_dict[i] = string.count(i)
    sorted(new_dict.keys())

    first_max = 0
    for key, values in new_dict.items():
        if values > first_max:
            first_max = values
            first_max_index = key
            first_max_count = values

    return first_max_index, first_max_count


print(count_repetition(data))
