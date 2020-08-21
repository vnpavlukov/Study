def make_array():
    a = []
    input_number = int(input())
    while input_number != 0:
        a.append(input_number)
        input_number = int(input())
    return a


def standard_deviation(array):
    sum_numbers = 0
    for i in array:
        sum_numbers += i
    s = sum_numbers / len(array)

    numerator = 0
    for x in array:
        numerator += (x - s) ** 2

    numerator /= (len(array) - 1)
    sigma = numerator ** 0.5
    return sigma


print(standard_deviation(make_array()))
