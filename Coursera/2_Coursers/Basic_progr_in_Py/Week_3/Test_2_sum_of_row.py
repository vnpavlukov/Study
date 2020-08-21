n = float(input())


def sum_of_raw(a):
    i = 1.0
    sum_numbers = 0
    while i <= a:
        sum_numbers += 1 / (i * i)
        i += 1
    return sum_numbers


print(sum_of_raw(n))
